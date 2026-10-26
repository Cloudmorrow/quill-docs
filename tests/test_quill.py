"""Docs' tests: the real record store, files and gate on this machine.

`cm quill test` runs them. Docs has no code: what is tested is that the
manifest installs, that everyone gets the welcome document, that a
document's blocks are kept exactly as written in its .docs file, and that
a Word file in the folder is read and written as one.
"""

import pytest

from cloudmorrow.quill.docs import Doc
from cloudmorrow.quill.testing import Harness


@pytest.fixture()
def q():
    with Harness(".") as harness:
        yield harness


IN_DOCUMENTS = {"share": "my-files", "within": "Documents", "suffix": ".docs,.docx"}


def test_everybody_gets_a_welcome_document_once(q):
    found = q.list("file", **IN_DOCUMENTS)
    assert [f["path"] for f in found] == ["Documents/Welcome.docs"], "the welcome document is seeded the first time"
    assert [f["path"] for f in q.list("file", **IN_DOCUMENTS)] == ["Documents/Welcome.docs"], "and only once"
    welcome = Doc.from_text(q.get("file", found[0].id)["text"])
    assert welcome.blocks[0] == {"kind": "heading", "level": 1, "runs": [{"text": "Welcome to Docs"}]}
    assert welcome.words > 60


def test_a_document_keeps_its_blocks_as_written(q):
    letter = Doc([
        {"kind": "heading", "level": 2, "runs": [{"text": "Offer"}]},
        {"kind": "paragraph", "align": "center", "runs": [{"text": "Ten "}, {"text": "percent", "bold": True}, {"text": " off"}]},
        {"kind": "numbered", "runs": [{"text": "until Friday"}]},
    ])
    made = q.seed("file", share="my-files", path="Documents/Offer.docs", text=letter.to_text())
    kept = q.get("file", made.id)["text"]
    assert kept == letter.to_text() and Doc.from_text(kept).blocks == letter.blocks


def test_a_word_file_is_a_document_too(q):
    """Written as text to a .docx path, the server writes Word's package;
    read back, the text is the same document."""
    q.list("file", **IN_DOCUMENTS)  # the welcome document first, as ever
    letter = Doc([{"kind": "heading", "level": 1, "runs": [{"text": "From Word"}]}, {"kind": "paragraph", "runs": [{"text": "Hello."}]}])
    made = q.seed("file", share="my-files", path="Documents/Letter.docx", text=letter.to_text())
    got = q.get("file", made.id)
    assert got["mime"] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    assert got["size"] > 1000, "Word's package, not the text"
    assert Doc.from_text(got["text"]).blocks == letter.blocks
    assert sorted(f["path"] for f in q.list("file", **IN_DOCUMENTS)) == ["Documents/Letter.docx", "Documents/Welcome.docs"]
