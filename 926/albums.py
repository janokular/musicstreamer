from pathlib import Path
from flask import current_app
from flask import url_for


def get_albums():
    albums = []
    base = Path(current_app.static_folder) / "albums"
    if not base.exists():
        return albums
    
    for artist_dir in base.iterdir():
        if not artist_dir.is_dir():
            continue
        artist = artist_dir.name

        for year_dir in artist_dir.iterdir():
            if not year_dir.is_dir():
                continue
            year_str = year_dir.name

            if not year_str.isdigit():
                continue
            year = int(year_str)

            for title_dir in year_dir.iterdir():
                if not title_dir.is_dir():
                    continue
                title = title_dir.name

                rel_path = f"albums/{artist}/{year_str}/{title}"
                url = url_for("static", filename=rel_path)

                albums.append({
                    "artist": artist.replace("_", " "),
                    "year": year,
                    "title": title.replace("_", " "),
                    "url": url,
                })

    albums.sort(key=lambda x: (x["artist"].lower(), x["year"], x["title"].lower()))
    return albums
  
