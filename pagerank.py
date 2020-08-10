import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    pagePointers = set()
    for x, y in corpus.items():
        if x == page:
            pagePointers = y
            break

    chances = dict()
    if len(pagePointers) == 0:
        chance = 1/len(corpus)
        for x in corpus:
            chances[x] = chance
        return chances

    chanceAmortecimento = (1-damping_factor)/(len(corpus))
    chanceComum = (damping_factor/len(pagePointers))
    for x in corpus:
        if x in pagePointers:
            chances[x] = chanceAmortecimento + chanceComum
        else:
            chances[x] = chanceAmortecimento

    return chances


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    visitedPages = []
    paginaAtual = random.choice(list(corpus.keys()))
    for i in range(n):
        chances = transition_model(corpus, paginaAtual, damping_factor)
        pageList = []
        pageChances = []
        for x, y in chances.items():
            pageList.append(x)
            pageChances.append(y)
        paginaAtual = random.choices(pageList, pageChances)[0]
        visitedPages.append(paginaAtual)

    oneFactor = 1/n
    pageRanks = dict()

    for page in corpus:
        pageRanks[page] = visitedPages.count(page) * oneFactor


    return pageRanks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    prs = dict()
    initialValue = 1/len(corpus)
    for x in corpus:
        prs[x] = initialValue

    altaDiferenca = True
    while altaDiferenca:
        altaDiferenca = False
        for x in prs:
            if recursive_pagerank(corpus, x, damping_factor, prs):
                altaDiferenca = True

    return prs

def recursive_pagerank(corpus, page, damping_factor, prs):
    somatorio = 0
    for i, links in corpus.items():
        if page in links:
            somatorio += prs[i]/len(links)

    pr = ((1-damping_factor)/len(corpus)) + damping_factor*somatorio
    if -0.001 < pr - prs[page] < 0.001:
        prs[page] = pr
        return False
    else:
        prs[page] = pr
        return True


if __name__ == "__main__":
    main()
