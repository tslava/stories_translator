import trafilatura

from src.utils import save_text_to_file


def extract_text(url):
    print(f"Extracting text from {url}...")
    downloaded = trafilatura.fetch_url(url)
    result = trafilatura.extract(
        downloaded,
        include_comments=False,
        target_language="pl",
        # favor_precision=True,
        # favor_recall=True,
    )

    filename = save_text_to_file('url_extracted_text', result)

    print(f"Done.\n")

    return result, filename


if __name__ == "__main__":
    # Example usage
    url = "https://zdrowie.trojmiasto.pl/Czy-drzemka-w-ciagu-dnia-jest-zdrowa-n185877.html"

    final_text = extract_text(url)

    print(f"Text extracted.")
