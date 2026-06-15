python
#!/usr/bin/env python3
"""
Axiom News Summarizer - CLI tool to fetch and summarize news articles
"""

import sys
import argparse
import requests
from datetime import datetime, timedelta
from typing import List, Dict
from newspaper import Article
from transformers import pipeline
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
import feedparser

console = Console()

class AxiomNewsSummarizer:
    """Fetch news from RSS feeds and generate AI summaries"""
    
    def __init__(self):
        console.print("[dim]🧠 Loading AI model (first time may take a moment)...[/dim]")
        self.summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            device=-1
        )
        
        self.feeds = {
            "elecciones": "https://news.google.com/rss/search?q=elecciones&hl=es&gl=ES&ceid=ES:es",
            "tecnologia": "https://news.google.com/rss/search?q=tecnología&hl=es&gl=ES&ceid=ES:es",
            "deportes": "https://news.google.com/rss/search?q=deportes&hl=es&gl=ES&ceid=ES:es",
            "economia": "https://news.google.com/rss/search?q=economía&hl=es&gl=ES&ceid=ES:es",
            "salud": "https://news.google.com/rss/search?q=salud&hl=es&gl=ES&ceid=ES:es",
            "internacional": "https://news.google.com/rss/search?q=internacional&hl=es&gl=ES&ceid=ES:es",
        }
    
    def fetch_articles(self, topic: str, limit: int = 3) -> List[Dict]:
        """Fetch articles for a given topic"""
        feed_url = self.feeds.get(topic.lower())
        if not feed_url:
            console.print(f"[red]❌ Topic '{topic}' not found. Available: {', '.join(self.feeds.keys())}[/red]")
            sys.exit(1)
        
        console.print(f"[bold cyan]🔍 Axiom scanning news about '{topic}'...[/bold cyan]")
        
        feed = feedparser.parse(feed_url)
        articles = []
        
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
            task = progress.add_task("Extracting articles...", total=limit)
            for entry in feed.entries[:limit]:
                try:
                    article = Article(entry.link)
                    article.download()
                    article.parse()
                    articles.append({
                        "title": article.title,
                        "text": article.text[:1024],
                        "url": entry.link,
                        "published": entry.get("published", "Unknown date")
                    })
                except Exception as e:
                    console.print(f"[yellow]⚠️ Skipping article: {e}[/yellow]")
                progress.update(task, advance=1)
        
        return articles
    
    def summarize_article(self, text: str) -> str:
        """Generate summary for a single article"""
        try:
            if len(text) > 1024:
                text = text[:1024]
            summary = self.summarizer(text, max_length=130, min_length=30, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"[red]Summarization failed: {e}[/red]"
    
    def run(self, topic: str):
        """Main execution flow"""
        console.print(Panel.fit(
            "[bold green]📰 AXIOM NEWS SUMMARIZER[/bold green]\n"
            "AI-powered intelligence from terminal",
            border_style="green"
        ))
        
        articles = self.fetch_articles(topic)
        
        if not articles:
            console.print("[red]No articles found.[/red]")
            sys.exit(1)
        
        console.print(f"\n[bold cyan]🎯 Top {len(articles)} intelligence items about '{topic}':[/bold cyan]\n")
        
        for idx, article in enumerate(articles, 1):
            console.print(Panel(
                f"[bold yellow]{article['title']}[/bold yellow]\n"
                f"[dim]📅 {article['published']}[/dim]\n\n"
                f"[bold green]🧠 Axiom Summary:[/bold green]\n"
                f"{self.summarize_article(article['text'])}\n\n"
                f"[dim]🔗 Source: {article['url']}[/dim]",
                title=f"📰 Item {idx}",
                border_style="blue"
            ))
            print()

def main():
    parser = argparse.ArgumentParser(
        description="Axiom News Summarizer - Get AI-powered news summaries",
        epilog="Example: axiom-news-summarizer tecnologia"
    )
    parser.add_argument(
        "topic",
        type=str,
        nargs="?",
        default="internacional",
        help="News topic (elecciones, tecnologia, deportes, economia, salud, internacional)"
    )
    args = parser.parse_args()
    
    summarizer = AxiomNewsSummarizer()
    summarizer.run(args.topic)

if __name__ == "__main__":
    main()

