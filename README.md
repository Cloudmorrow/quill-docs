# Docs

A Quill for [Cloudmorrow](https://github.com/Cloudmorrow/cloudmorrow): a
basic Word — documents of headings, paragraphs, lists, quotes and tables,
with bold, italic, underline, strike-through and links — on the phone, the
web app, the terminal and the command line.

- A document is a page you type into. The bar above it puts a style on what
  you have selected: a heading, bold, a list, a quote, a link, how a line
  is aligned. It saves as you type.
- A document is a `.docs` file in the `Documents` folder of your drive on
  the server: a plain text file holding its blocks exactly as written — in
  My Files, on WebDAV, in a backup of the folder, open to `cm`, to your
  assistant, and to anything that reads JSON. Docs is the kit's document
  over those files and nothing more. Removing this Quill takes the tab
  away, never a document.
- A Word file (`.docx`) in that folder is a document too: it opens here,
  and is saved back as Word. What the kit keeps — the words, the styles
  above — goes to and from Word; pictures, fonts, sizes and colours do not.
- **Export** hands any document to you as Word, as a PDF, or as Markdown.
  **Open** opens a document from anywhere on your cloud — another folder
  of your drive, a fileshare, a Word file somebody put there — and it
  stays where it is.
- In the terminal and on the command line a document is edited as
  Markdown (`# ` a heading, `- ` a bullet, `**bold**`), imported from a
  Word, `.docs` or Markdown file on this machine, and exported to Word,
  PDF, `.docs` or Markdown; `cm docs show team:Plans/Offer.docx` reaches
  a document anywhere.
- Folders under Documents, a search through names and words, and a first
  document, Welcome, for everyone the first time they open Docs.

The file, what goes to and from Word, and what each surface does, are
[docs/DOCS.md](https://github.com/Cloudmorrow/cloudmorrow/blob/main/docs/DOCS.md)
in the Cloudmorrow repository.

Install it from the Quill Catalog, or from this repository with
`cm quill add --source https://github.com/Cloudmorrow/quill-docs --ref v1.1.0`.

## What it adds to your Cloudmorrow

`cm quill check` prints this for you; keep it here for the catalog page.

| | |
| --- | --- |
| Datamodels | uses `file` |
| Screens | Docs: the folders and documents, and one open as a page — on the phone, the web app, the terminal, `cm docs`, and to your assistant |
| Datasets | a first document, `Documents/Welcome.docs`, for everyone once |
| Code | none |

## On the command line

```
cm docs list                            # every document, folders and all; Word ones say so
cm docs show Letter                     # as Markdown; --raw the file's text; --plain the record
cm docs add Letter                      # a new document, from stdin or $EDITOR, as Markdown
cm docs add Letter "# Hi" "words"       # or from the lines given
cm docs edit Letter                     # $EDITOR with the Markdown, or the new Markdown from stdin
cm docs search invoice                  # names and words
cm docs set Letter name=Offer           # renames the file; path=2026/Offer moves it to a folder that is there
cm docs export Letter                   # Letter.docx here; or a name ending .docx, .docs or .md
cm docs import ./Offer.docx [2026/Offer]   # a Word, .docs or Markdown file, as a document
cm docs delete Letter
```

## Working on it

```
uv sync                  # .venv with Cloudmorrow and pytest
cm quill check           # the manifest, as a server would install it
cm quill test            # tests/, against the real record store and gate
cm quill dev --local     # a throwaway server here, reinstalled as you save
```
