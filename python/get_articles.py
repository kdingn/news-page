import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_aidb():
    url = "https://aiboom.net"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, features="html.parser")
    article = list(
        map(
            lambda x: {
                "date": x.find(class_="entry-date updated").text,
                "title": x.find(class_="title").text,
                "link": x.find(class_="link").get("href"),
            },
            soup.find_all(class_="post_item clearfix"),
        )
    )
    df = pd.DataFrame(article).sort_values(["date", "link"])
    df["date"] = pd.to_datetime(df["date"])
    df["source"] = "aidb"
    return df


def main():
    df = pd.read_csv("src/assets/articles.csv")
    df["date"] = pd.to_datetime(df["date"])
    df = pd.concat([df, get_aidb()])
    df = (
        df.sort_values("date", ascending=False)
        .drop_duplicates("link", keep="first")
        .reset_index(drop=True)
    )
    df.to_csv("src/assets/articles.csv", index=False)


if __name__ == "__main__":
    main()
