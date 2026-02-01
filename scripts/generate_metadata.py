import os
import pandas as pd
from PyPDF2 import PdfReader

# -----------------------------
# CONFIG
# -----------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CSV_FILE = os.path.join(BASE_DIR, 'oTree_export.csv')

PDF_FOLDERS = {
    "en": os.path.join(BASE_DIR, 'research_design_rater', 'static', 'research_design_rater', 'designs', 'pdf_en'),
    "de": os.path.join(BASE_DIR, 'research_design_rater', 'static', 'research_design_rater', 'designs', 'pdf_de')
}

OUTPUT_FOLDERS = {
    "en": os.path.join(BASE_DIR, 'arcana_en'),
    "de": os.path.join(BASE_DIR, 'arcana_de')
}

# Make sure output folders exist
for folder in OUTPUT_FOLDERS.values():
    os.makedirs(folder, exist_ok=True)

# -----------------------------
# LOAD CSV
# -----------------------------
df = pd.read_csv(CSV_FILE)

# -----------------------------
# PROCESS CSV
# -----------------------------

all_files = {}

for lang, pdf_dir in PDF_FOLDERS.items():
    pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    for pdf_file in pdf_files:
        # Collect all ratings and comments for this PDF
        ratings = []
        comments = []

        # Loop through all columns to find ratings/comments for this PDF
        for col in df.columns:
            if col.endswith('.player.rating'):
                pdf_col = col.replace('.player.rating', '.player.experiment_title')
                for idx, val in enumerate(df[pdf_col]):
                    if str(val).strip() == pdf_file:
                        rating = df.at[idx, col]
                        if not pd.isna(rating):
                            ratings.append(rating)

                        comment_col = col.replace('.rating', '.comment')
                        comment = df.at[idx, comment_col]
                        if not pd.isna(comment):
                            comments.append(str(comment))

        if ratings:
            avg_rating = sum(ratings) / len(ratings)
        else:
            avg_rating = 0

        num_ratings = len(ratings)

        # Read number of pages from PDF
        pdf_path = os.path.join(pdf_dir, pdf_file)
        try:
            reader = PdfReader(pdf_path)
            num_pages = len(reader.pages)
        except Exception:
            num_pages = 0

        # Save all metadata
        all_files[pdf_file] = {
            "title": pdf_file.replace('.pdf', ''),
            "comments": comments,
            "avg_rating": avg_rating,
            "num_ratings": num_ratings,
            "num_pages": num_pages,
            "language": lang
        }

# -----------------------------
# GENERATE METADATA FILES
# -----------------------------
for fn, data in all_files.items():
    out_dir = OUTPUT_FOLDERS[data['language']]

    comments_text = "\n".join(data['comments'])
    quality = "high" if data['avg_rating'] >= 4 else "low"

    md_content = f"""---
author: local
title: {data['title']}
description: ""
filename: {fn}
extension: MarkdownPlus
number_of_pages: {data['num_pages']}
version: 1.0
language: {data['language']}
type: student_design
visibility: student
average_rating: {data['avg_rating']:.2f}
number_of_ratings: {data['num_ratings']}
quality_tier: {quality}
---

{comments_text}
"""

    # Save to output folder
    out_file = os.path.join(out_dir, fn.replace('.pdf', '.md'))
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

print("Metadata generation finished!")


