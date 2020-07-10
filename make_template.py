"""Code adapted from https://gist.github.com/neighthan/e7d088ab752ece583ffc16178ac0d9b4."""
import requests
from datetime import datetime
from raschietto import Raschietto, Matcher
from argparse import ArgumentParser
from os.path import realpath, join, exists
from email.utils import parsedate


def main():
    parser = ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("short_title", help="Short title for paper; used to name file.")
    parser.add_argument("-j", "--journal", help="Journal published in [default = arXiv if 'arxiv' in url else '']",
                        default="")
    args = parser.parse_args()

    journal = "arXiv" if "arxiv" in args.url and not args.journal else args.journal

    paper_data = {}
    paper_data["url"] = args.url
    paper_data["added_date"] = str(datetime.now().date())
    paper_data["short_title"] = args.short_title
    paper_data["journal"] = journal

    if "arxiv" in args.url:
        paper_data.update(extract_arxiv_data(args.url))
    else:
        paper_data.update({
            "title": "",
            "authors": "[]",
            "year": int(paper_data["added_date"].split("-")[0]),
            "arxiv_id": "",
        })

    papers_dir = realpath(join(__file__, ".."))

    with open(join(papers_dir, "template.md")) as f:
        template = f.read()

    template = template.format(**paper_data)

    new_paper_fname = join(papers_dir, args.short_title + ".md")

    if exists(new_paper_fname):
        overwrite = input(f"Overwrite existing file {new_paper_fname} (y/n)? ")
        if overwrite != "y":
            return

    with open(new_paper_fname, "w") as f:
        f.write(template)


def extract_arxiv_data(url):
    paper_data = {}

    page = Raschietto.from_url(url)

    title_matcher = Matcher("#abs > h1",
                            mapping=lambda element, page: Raschietto.element_to_text(element)[6:])
    authors_matcher = Matcher("#abs > div.authors",
                              mapping=lambda element, page: Raschietto.element_to_text(element)[8:].split(", "))
    year_matcher = Matcher("#abs > div.dateline",
                           mapping=lambda element, page: Raschietto.element_to_text(element))

    paper_data["title"] = title_matcher(page)
    paper_data["authors"] = authors_matcher(page)

    year = year_matcher(page)
    paper_data["year"] = year[year.rfind("20"):year.rfind("20") + 4]

    paper_data["arxiv_id"] = url[url.find("abs") + 4:]
    return paper_data


if __name__ == "__main__":
    main()
