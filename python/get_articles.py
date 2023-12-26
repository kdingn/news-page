import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_ogimage(df):
    print(f"{len(df)} new articles")
    images = []
    for link in df["link"]:
        soup = BeautifulSoup(requests.get(link).content, features="html.parser")
        thumb = soup.find('meta', attrs={'property': 'og:image'}).get("content")
        images.append(thumb)
        time.sleep(1)
    df["ogimage"] = images
    return df


def get_aidb(df_org):
    url = "https://aiboom.net"
    soup = BeautifulSoup(requests.get(url).content, features="html.parser")
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
    df = df[df["link"].apply(lambda x: x not in df_org["link"])]
    df = get_ogimage(df)
    return df


def main():
aa
    df = pd.read_csv("src/assets/articles.csv")
    df["date"] = pd.to_datetime(df["date"])
    df = pd.concat([df, get_aidb(df)])
    df = (
        df.sort_values("date", ascending=False)
        .drop_duplicates("link", keep="first")
        .reset_index(drop=True)
    )
    df.to_csv("src/assets/articles.csv", index=False)


if __name__ == "__main__":
    main()
