import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_ogimage(df):
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
                "date": x.find(class_="entry-date updated").get_text(strip=True),
                "title": x.find(class_="title").get_text(strip=True),
                "link": x.find(class_="link").get("href"),
            },
            soup.find_all(class_="post_item clearfix"),
        )
    )
    df = pd.DataFrame(article).sort_values(["date", "link"])
    df["date"] = pd.to_datetime(df["date"])
    df["source"] = "AIDB"
    df = df[df["date"] >= df_org[df_org["source"]=="AIDB"]["date"].max()].drop_duplicates("link")
    df = get_ogimage(df)
    return df


def main():
    df = pd.read_csv("src/assets/articles.csv")
    df["date"] = pd.to_datetime(df["date"])
    df = pd.concat([df, get_aidb(df)])
    df = (
        df.sort_values(["date", "link"], ascending=False)
        .drop_duplicates("link", keep="first")
        .reset_index(drop=True)
    )
    df.to_csv("src/assets/articles.csv", index=False)


if __name__ == "__main__":
    main()
