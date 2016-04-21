bible = dict()

books = []

with open("kjv.atv") as bible_file:
    for line in bible_file:
        line = line.rstrip()
        parts = line.split("@")
        book = parts[0]
        reference = parts[1]
        verse_text = parts[2]

        (chapter, verse) = reference.split(":")
        chapter = int(chapter)
        verse = int(verse)

        if book in bible:
           book_chapters = bible[book]
        else:
           book_chapters = [ ]
           bible[book] = book_chapters
           books.append(book)

        if len(book_chapters) >= chapter:
            book_chapters[chapter-1].append(verse_text)
        else:
            book_chapters.append ([verse_text])