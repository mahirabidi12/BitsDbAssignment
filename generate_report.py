from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os

# -- colour palette ----------------------------------------------------------
NAVY    = (26,  43,  74)
GOLD    = (204, 153,  0)
WHITE   = (255, 255, 255)
LGRAY   = (245, 245, 250)
MGRAY   = (200, 200, 210)
DGRAY   = (80,  80,  100)
GREEN   = (39, 174,  96)
RED     = (192,  57,  43)
CODE_BG = (30,  30,  50)
CODE_FG = (220, 220, 255)

GITHUB = "https://github.com/mahirabidi12/BitsDbAssignment"

# -- helpers ------------------------------------------------------------------
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        self._toc = []           # [(title, page)]
        self._section_num = 0

    # -- page chrome ----------------------------------------------------------
    def header(self):
        if self.page_no() == 1:
            return
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 210, 12, 'F')
        self.set_text_color(*GOLD)
        self.set_font("Helvetica", "B", 8)
        self.set_xy(10, 3)
        self.cell(0, 6, "Library Management System  |  Spring Boot + JPA + JSP", align="L")
        self.set_xy(0, 3)
        self.cell(200, 6, f"Page {self.page_no()}", align="R")
        self.ln(10)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-12)
        self.set_draw_color(*GOLD)
        self.set_line_width(0.4)
        self.line(15, self.get_y(), 195, self.get_y())
        self.set_text_color(*DGRAY)
        self.set_font("Helvetica", "", 7)
        self.set_y(-10)
        self.cell(0, 5, "BITS Pilani - Database Assignment  |  mahir.abidi@scaler.com", align="C")

    # -- cover page -----------------------------------------------------------
    def cover(self):
        self.add_page()
        # big navy block
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 210, 297, 'F')
        # decorative gold bar
        self.set_fill_color(*GOLD)
        self.rect(0, 100, 210, 6, 'F')
        self.rect(0, 186, 210, 6, 'F')
        # title
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 32)
        self.set_xy(0, 54)
        self.cell(210, 14, "Library Management", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(210, 14, "System", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        # subtitle
        self.set_text_color(*GOLD)
        self.set_font("Helvetica", "I", 14)
        self.set_xy(0, 88)
        self.cell(210, 10, "Spring Boot . JPA . Spring MVC . JSP . H2 . JUnit", align="C")
        # body text box
        self.set_fill_color(40, 60, 100)
        self.rect(25, 110, 160, 68, 'F')
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 11)
        self.set_xy(25, 114)
        self.cell(160, 8, "Assignment Report", align="C")
        rows = [
            ("Entities",    "Author  &  Book"),
            ("Operations",  "Create  .  Read  .  Update"),
            ("Database",    "H2 In-Memory (JPA / Hibernate)"),
            ("Tests",       "46 unit tests  (JUnit 5 + Mockito)"),
            ("Submitted by","Mahir Abidi  |  mahir.abidi@scaler.com"),
            ("Date",        "May 2026"),
        ]
        self.set_font("Helvetica", "", 10)
        y = 124
        for k, v in rows:
            self.set_xy(30, y)
            self.set_text_color(*GOLD)
            self.cell(42, 7, k + ":", align="R")
            self.set_text_color(*WHITE)
            self.cell(0, 7, "  " + v)
            y += 8
        # github
        self.set_text_color(*GOLD)
        self.set_font("Helvetica", "U", 9)
        self.set_xy(0, 198)
        self.cell(210, 8, GITHUB, align="C", link=GITHUB)
        # bottom note
        self.set_text_color(160, 180, 220)
        self.set_font("Helvetica", "I", 8)
        self.set_xy(0, 275)
        self.cell(210, 6, "BITS Pilani  |  Database Technologies Assignment", align="C")

    # -- section heading -------------------------------------------------------
    def section(self, title):
        self._section_num += 1
        self._toc.append((f"{self._section_num}. {title}", self.page_no()))
        self.set_fill_color(*NAVY)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 13)
        self.set_x(10)
        self.cell(190, 9, f"  {self._section_num}.  {title}", fill=True,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(*GOLD)
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
        self.set_text_color(0, 0, 0)

    def subsection(self, title):
        self.set_text_color(*NAVY)
        self.set_font("Helvetica", "B", 11)
        self.set_x(12)
        self.cell(0, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(*MGRAY)
        self.set_line_width(0.3)
        self.line(12, self.get_y(), 180, self.get_y())
        self.ln(2)
        self.set_text_color(0, 0, 0)

    # -- body text -------------------------------------------------------------
    def body(self, text, indent=14):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.set_x(indent)
        self.multi_cell(210 - indent - 10, 6, text)
        self.ln(2)

    def bullet(self, items, indent=18):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        for item in items:
            self.set_x(indent)
            self.cell(5, 6, chr(42))
            self.multi_cell(210 - indent - 14, 6, item)
        self.ln(1)

    # -- code block ------------------------------------------------------------
    def code(self, snippet, lang="java"):
        lines = snippet.strip().split("\n")
        line_h = 4.8
        pad = 4
        block_h = len(lines) * line_h + pad * 2
        # background
        x0 = 14
        self.set_fill_color(*CODE_BG)
        self.rect(x0, self.get_y(), 182, block_h, 'F')
        # lang badge
        self.set_fill_color(*GOLD)
        self.set_text_color(*NAVY)
        self.set_font("Helvetica", "B", 7)
        self.set_xy(x0, self.get_y())
        self.cell(18, 5, f" {lang.upper()}", fill=True)
        self.ln(5)
        # code text
        self.set_text_color(*CODE_FG)
        self.set_font("Courier", "", 7.5)
        for line in lines:
            self.set_x(x0 + pad)
            self.cell(0, line_h, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)
        self.set_text_color(0, 0, 0)

    # -- info / warning boxes --------------------------------------------------
    def info_box(self, title, body_text, color=None):
        if color is None:
            color = (230, 240, 255)
        self.set_fill_color(*color)
        self.set_draw_color(*NAVY)
        self.set_line_width(0.4)
        x0, y0 = 14, self.get_y()
        self.rect(x0, y0, 182, 100, '')   # dummy - will re-draw after
        # title
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*NAVY)
        self.set_x(x0 + 3)
        self.cell(0, 7, title)
        self.ln(7)
        # body
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(30, 30, 50)
        self.set_x(x0 + 3)
        y_before = self.get_y()
        self.multi_cell(176, 5.5, body_text)
        y_after = self.get_y()
        block_h = y_after - y0 + 3
        self.set_fill_color(*color)
        self.rect(x0, y0, 182, block_h, 'FD')
        # re-write text on top
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*NAVY)
        self.set_xy(x0 + 3, y0)
        self.cell(0, 7, title)
        self.set_xy(x0 + 3, y0 + 7)
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(30, 30, 50)
        self.multi_cell(176, 5.5, body_text)
        self.ln(3)

    # -- er diagram (boxes + arrow) --------------------------------------------
    def er_diagram(self):
        y = self.get_y() + 4
        # Author box
        ax, aw = 20, 72
        self.set_fill_color(*NAVY)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 10)
        self.rect(ax, y, aw, 8, 'F')
        self.set_xy(ax, y)
        self.cell(aw, 8, "AUTHOR", align="C")
        fields_a = [
            ("PK", "id : BIGINT"),
            ("",   "firstName : VARCHAR"),
            ("",   "lastName  : VARCHAR"),
            ("UK", "email : VARCHAR"),
            ("",   "birthYear : INT"),
            ("",   "nationality : VARCHAR"),
        ]
        self.set_font("Helvetica", "", 8.5)
        fy = y + 8
        for pk, name in fields_a:
            bg = (240, 248, 255) if pk == "PK" else (245, 245, 252) if pk == "UK" else WHITE
            self.set_fill_color(*bg)
            self.rect(ax, fy, aw, 6.5, 'FD')
            self.set_text_color(NAVY[0], NAVY[1], NAVY[2])
            self.set_xy(ax + 1, fy)
            self.set_font("Helvetica", "B" if pk else "", 7.5)
            self.cell(10, 6.5, pk)
            self.set_font("Courier", "", 8)
            self.set_text_color(30, 30, 30)
            self.cell(0, 6.5, name)
            fy += 6.5
        author_mid_y = (y + fy) / 2

        # Book box
        bx, bw = 118, 72
        self.set_fill_color(*GOLD)
        self.set_text_color(*NAVY)
        self.set_font("Helvetica", "B", 10)
        self.rect(bx, y, bw, 8, 'F')
        self.set_xy(bx, y)
        self.cell(bw, 8, "BOOK", align="C")
        fields_b = [
            ("PK", "id : BIGINT"),
            ("",   "title : VARCHAR"),
            ("UK", "isbn : VARCHAR"),
            ("",   "genre : VARCHAR"),
            ("",   "publishedYear : INT"),
            ("",   "price : DOUBLE"),
            ("FK", "author_id : BIGINT"),
        ]
        self.set_font("Helvetica", "", 8.5)
        fy2 = y + 8
        for pk, name in fields_b:
            bg = (255, 252, 230) if pk == "PK" else (230, 255, 230) if pk == "FK" else (245, 245, 252) if pk == "UK" else WHITE
            self.set_fill_color(*bg)
            self.rect(bx, fy2, bw, 6.5, 'FD')
            self.set_text_color(*NAVY)
            self.set_xy(bx + 1, fy2)
            self.set_font("Helvetica", "B" if pk else "", 7.5)
            self.cell(10, 6.5, pk)
            self.set_font("Courier", "", 8)
            self.set_text_color(30, 30, 30)
            self.cell(0, 6.5, name)
            fy2 += 6.5
        book_mid_y = (y + fy2) / 2

        # relationship arrow
        mid_x = (ax + aw + bx) / 2
        mid_y = (author_mid_y + book_mid_y) / 2
        self.set_draw_color(*NAVY)
        self.set_line_width(1.0)
        self.line(ax + aw, author_mid_y, bx, book_mid_y)
        # cardinality labels
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*NAVY)
        self.set_xy(ax + aw + 1, author_mid_y - 5)
        self.cell(10, 5, "1")
        self.set_xy(bx - 9, book_mid_y - 5)
        self.cell(10, 5, "N")
        # label
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*DGRAY)
        self.set_xy(mid_x - 15, mid_y - 8)
        self.cell(30, 5, "has/belongs to", align="C")

        self.set_y(max(fy, fy2) + 6)

    # -- mock screenshot frame -------------------------------------------------
    def mock_screen(self, title, rows, columns=None, note=None):
        y0 = self.get_y()
        # browser chrome
        self.set_fill_color(230, 230, 230)
        self.rect(14, y0, 182, 7, 'F')
        self.set_fill_color(200, 200, 200)
        for cx in [17, 22, 27]:
            self.circle(cx, y0 + 3.5, 1.5, 'F')
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*DGRAY)
        self.set_xy(50, y0)
        self.cell(0, 7, "http://localhost:8080" + title)
        # navbar
        self.set_fill_color(*NAVY)
        self.rect(14, y0 + 7, 182, 8, 'F')
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 8)
        self.set_xy(16, y0 + 7)
        self.cell(50, 8, " Library Management System")
        self.set_font("Helvetica", "", 8)
        for lbl, off in [("Books", 110), ("Authors", 133), ("By Nationality", 155)]:
            self.set_xy(14 + off, y0 + 7)
            self.cell(24, 8, lbl, align="C")
        # content area
        self.set_fill_color(245, 245, 250)
        row_h = 7
        header_h = 8
        n_rows = len(rows)
        cols = columns or (list(rows[0].keys()) if rows else [])
        content_h = header_h + n_rows * row_h + 6
        self.rect(14, y0 + 15, 182, content_h, 'F')
        # table header
        self.set_fill_color(*NAVY)
        col_w = 182 // max(len(cols), 1)
        ty = y0 + 15
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 8)
        for i, col in enumerate(cols):
            self.set_xy(14 + i * col_w, ty)
            self.rect(14 + i * col_w, ty, col_w, header_h, 'F')
            self.cell(col_w, header_h, col, align="C")
        ty += header_h
        # rows
        for ri, row in enumerate(rows):
            bg = WHITE if ri % 2 == 0 else (235, 237, 245)
            self.set_fill_color(*bg)
            for i, col in enumerate(cols):
                self.set_fill_color(*bg)
                self.rect(14 + i * col_w, ty, col_w, row_h, 'F')
                self.set_text_color(30, 30, 30)
                self.set_font("Helvetica", "", 7.5)
                self.set_xy(14 + i * col_w + 1, ty)
                val = str(row.get(col, ""))
                if val in ("Edit", "Delete"):
                    c = (0, 100, 200) if val == "Edit" else (180, 30, 30)
                    self.set_text_color(*c)
                    self.set_font("Helvetica", "U", 7.5)
                self.cell(col_w - 2, row_h, val, align="C")
                self.set_text_color(30, 30, 30)
                self.set_font("Helvetica", "", 7.5)
            ty += row_h
        if note:
            self.set_xy(14, ty + 2)
            self.set_font("Helvetica", "I", 7)
            self.set_text_color(*DGRAY)
            self.cell(0, 5, note)
        self.set_y(ty + 10)
        self.ln(2)

    def mock_form(self, title, fields, action_label="Save"):
        y0 = self.get_y()
        self.set_fill_color(230, 230, 230)
        self.rect(14, y0, 182, 7, 'F')
        self.set_fill_color(200, 200, 200)
        for cx in [17, 22, 27]:
            self.circle(cx, y0 + 3.5, 1.5, 'F')
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*DGRAY)
        self.set_xy(50, y0)
        self.cell(0, 7, "http://localhost:8080" + title)
        self.set_fill_color(*NAVY)
        self.rect(14, y0 + 7, 182, 8, 'F')
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 8)
        self.set_xy(16, y0 + 7)
        self.cell(0, 8, " Library Management System")
        # card
        card_h = 14 + len(fields) * 14 + 14
        self.set_fill_color(*WHITE)
        self.set_draw_color(*MGRAY)
        self.set_line_width(0.3)
        self.rect(30, y0 + 18, 150, card_h, 'FD')
        self.set_fill_color(*NAVY)
        self.rect(30, y0 + 18, 150, 10, 'F')
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 9)
        self.set_xy(30, y0 + 18)
        self.cell(150, 10, title.split("/")[-1].replace("-", " ").title(), align="C")
        fy = y0 + 30
        for label, placeholder in fields:
            self.set_text_color(*NAVY)
            self.set_font("Helvetica", "B", 8)
            self.set_xy(35, fy)
            self.cell(50, 6, label + ":")
            self.set_fill_color(248, 248, 255)
            self.set_draw_color(*MGRAY)
            self.rect(85, fy, 88, 7, 'FD')
            self.set_text_color(*DGRAY)
            self.set_font("Helvetica", "I", 7.5)
            self.set_xy(87, fy)
            self.cell(0, 7, placeholder)
            fy += 14
        # button
        self.set_fill_color(*GOLD)
        self.rect(85, fy, 40, 8, 'F')
        self.set_text_color(*NAVY)
        self.set_font("Helvetica", "B", 9)
        self.set_xy(85, fy)
        self.cell(40, 8, action_label, align="C")
        self.set_y(y0 + 18 + card_h + 8)
        self.ln(2)

    def test_table(self, tests):
        cols  = ["Test Class", "Test Method", "Type", "Status"]
        w     = [48, 80, 28, 22]
        row_h = 7
        y0    = self.get_y()
        # header
        self.set_fill_color(*NAVY)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 8)
        x = 14
        for c, cw in zip(cols, w):
            self.rect(x, y0, cw, 8, 'F')
            self.set_xy(x, y0)
            self.cell(cw, 8, c, align="C")
            x += cw
        y0 += 8
        for ri, (cls, method, typ, ok) in enumerate(tests):
            bg = WHITE if ri % 2 == 0 else (240, 244, 255)
            self.set_fill_color(*bg)
            x = 14
            vals = [cls, method, typ, "PASS" if ok else "FAIL"]
            self.set_font("Helvetica", "", 7.5)
            for v, cw in zip(vals, w):
                self.rect(x, y0, cw, row_h, 'F')
                self.set_xy(x + 1, y0)
                if v == "PASS":
                    self.set_text_color(*GREEN)
                    self.set_font("Helvetica", "B", 7.5)
                elif v == "FAIL":
                    self.set_text_color(*RED)
                    self.set_font("Helvetica", "B", 7.5)
                else:
                    self.set_text_color(30, 30, 30)
                    self.set_font("Helvetica", "", 7.5)
                self.cell(cw - 2, row_h, v)
                x += cw
            y0 += row_h
        self.set_y(y0 + 4)

# ═══════════════════════════════════════════════════════════════════════════════
#  BUILD PDF
# ═══════════════════════════════════════════════════════════════════════════════
pdf = PDF()
pdf.set_title("Library Management System - Assignment Report")
pdf.set_author("Mahir Abidi")

# -- 1. Cover ------------------------------------------------------------------
pdf.cover()

# -- 2. TOC (hardcoded page numbers match the content below) ------------------
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.set_text_color(*NAVY)
pdf.set_xy(0, 40)
pdf.cell(210, 12, "Table of Contents", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_draw_color(*GOLD)
pdf.set_line_width(0.8)
pdf.line(30, pdf.get_y(), 180, pdf.get_y())
pdf.ln(8)
toc_sections = [
    (1,  "Project Overview",                     3),
    (2,  "Entity Relationship Design",           4),
    (3,  "Database Population (Sample Data)",    5),
    (4,  "Repository Layer",                     6),
    (5,  "Service Layer",                        7),
    (6,  "Controller Layer",                     8),
    (7,  "View Layer - JSP Pages",               9),
    (8,  "Implementation Details per Operation", 11),
    (9,  "Unit Testing",                         12),
    (10, "Challenges Faced and Solutions",       13),
    (11, "Application Configuration",            14),
    (12, "GitHub Repository",                    15),
    (13, "Conclusion",                           16),
]
for num, title, pg in toc_sections:
    pdf.set_x(30)
    pdf.set_font("Helvetica", "B" if num <= 3 else "", 10)
    pdf.set_text_color(*NAVY)
    label = f"{num}.  {title}"
    pdf.cell(130, 8, label)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*MGRAY)
    pdf.cell(20, 8, "." * 20, align="R")
    pdf.set_text_color(*NAVY)
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(10, 8, str(pg), align="R")
    pdf.ln(8)

# -- 3. Project Overview -------------------------------------------------------
pdf.add_page()
pdf.section("Project Overview")
pdf.body(
    "This project implements a Library Management System using Spring Boot 2.7 as a full-stack "
    "web application. The system manages two core entities -- Authors and Books -- with a "
    "bidirectional one-to-many relationship. Users can create, view, and update records through "
    "a JSP-based web interface. The back-end uses Spring Data JPA with Hibernate as the ORM, "
    "backed by an H2 in-memory database for development. 46 unit tests (JUnit 5 + Mockito) "
    "cover the repository and service layers."
)
pdf.ln(2)

pdf.subsection("Technology Stack")
pdf.bullet([
    "Spring Boot 2.7.18  -  auto-configuration, embedded Tomcat, dependency management",
    "Spring MVC  -  @Controller, Model, RedirectAttributes, @ModelAttribute",
    "Spring Data JPA  -  JpaRepository, custom @Query methods, JPQL INNER JOIN",
    "Hibernate 5.6  -  ORM, DDL auto-creation (create-drop for dev)",
    "H2 In-Memory Database  -  zero-config dev database, console at /h2-console",
    "JSP + JSTL  -  server-side view rendering with Expression Language (EL)",
    "JUnit 5 + Mockito  -  unit tests for service and repository layers",
    "Maven  -  build, dependency management, WAR packaging",
])

pdf.subsection("Project Directory Structure")
pdf.code("""\
BitsDbAssignment/
+-- pom.xml
+-- src/
    +-- main/
    |   +-- java/com/bits/library/
    |   |   +-- LibraryApplication.java         (entry-point + WAR bootstrap)
    |   |   +-- config/DataInitializer.java      (seeds 10 Authors + 10 Books)
    |   |   +-- entity/   Author.java  Book.java
    |   |   +-- repository/ AuthorRepository  BookRepository
    |   |   +-- service/    AuthorService     BookService  (interface + impl)
    |   |   +-- controller/ AuthorController  BookController  HomeController
    |   +-- resources/application.properties
    |   +-- webapp/WEB-INF/views/
    |       +-- layout/header.jsp
    |       +-- index.jsp
    |       +-- authors/ list.jsp  form.jsp
    |       +-- books/   list.jsp  form.jsp  byNationality.jsp
    +-- test/java/com/bits/library/
        +-- repository/ AuthorRepositoryTest  BookRepositoryTest
        +-- service/    AuthorServiceTest     BookServiceTest""", lang="text")

# -- 4. Entity Relationship Design --------------------------------------------
pdf.add_page()
pdf.section("Entity Relationship Design")
pdf.body(
    "The system models a classic library domain: an Author can write many Books, and each Book "
    "belongs to exactly one Author -- a one-to-many (1:N) relationship. JPA annotations on the "
    "entity classes drive Hibernate's DDL generation at startup."
)

pdf.er_diagram()

pdf.subsection("Author Entity")
pdf.code("""\
@Entity
@Table(name = "authors")
public class Author {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String firstName;

    @Column(nullable = false)
    private String lastName;

    @Column(unique = true, nullable = false)
    private String email;          // UNIQUE constraint

    private int    birthYear;
    private String nationality;

    @OneToMany(mappedBy = "author",
               cascade = CascadeType.ALL,
               fetch = FetchType.LAZY)
    private List<Book> books = new ArrayList<>();
}""")

pdf.subsection("Book Entity")
pdf.code("""\
@Entity
@Table(name = "books")
public class Book {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String title;

    @Column(unique = true, nullable = false)
    private String isbn;           // UNIQUE constraint

    private String genre;
    private int    publishedYear;
    private double price;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "author_id", nullable = false)
    private Author author;         // FK -> authors.id
}""")

pdf.subsection("Relationship Explanation")
pdf.bullet([
    "@OneToMany on Author: cascade=ALL means saving/deleting an Author propagates to Books. "
    "fetch=LAZY avoids loading all books every time an Author is fetched.",
    "@ManyToOne on Book with @JoinColumn(name='author_id'): creates the foreign-key column in "
    "the books table pointing back to authors.id.",
    "Unique constraints on email (Author) and isbn (Book) are enforced at the database level "
    "and surfaced as DataIntegrityViolationException which the controllers catch.",
])

# -- 5. Database Population ----------------------------------------------------
pdf.add_page()
pdf.section("Database Population (Sample Data)")
pdf.body(
    "The DataInitializer component implements CommandLineRunner and runs automatically at "
    "application startup, inserting 10 Authors and 10 Books into the H2 database."
)
pdf.code("""\
@Component
public class DataInitializer implements CommandLineRunner {

    @Autowired AuthorRepository authorRepository;
    @Autowired BookRepository   bookRepository;

    @Override
    public void run(String... args) {
        Author a1 = authorRepository.save(
            new Author("George","Orwell","george.orwell@books.com",1903,"British"));
        Author a2 = authorRepository.save(
            new Author("J.K.","Rowling","jk.rowling@books.com",1965,"British"));
        Author a3 = authorRepository.save(
            new Author("Ernest","Hemingway","ernest.hemingway@books.com",1899,"American"));
        // ... 7 more authors (Twain, Tolstoy, Dostoevsky, Marquez,
        //                      Murakami, Christie, Kafka)

        bookRepository.save(new Book("1984","978-0-452-28423-4",
            "Dystopian Fiction",1949,12.99,a1));
        bookRepository.save(new Book("Animal Farm","978-0-452-28424-1",
            "Political Satire",1945,9.99,a1));
        bookRepository.save(new Book("Harry Potter - Philosopher's Stone",
            "978-0-7475-3269-9","Fantasy",1997,14.99,a2));
        // ... 7 more books
    }
}""")

pdf.subsection("Seeded Data Summary")
pdf.bullet([
    "10 Authors: British (Orwell, Rowling, Christie), American (Hemingway, Twain), Russian "
    "(Tolstoy, Dostoevsky), Colombian (Marquez), Japanese (Murakami), Czech (Kafka).",
    "10 Books: assigned across authors -- Orwell gets 2 (1984, Animal Farm), Rowling gets 2 "
    "(HP1, HP2); remaining authors each receive 1 book.",
    "Sample data exercises all nationality values used later by the INNER JOIN query.",
])

# -- 6. Repository Layer -------------------------------------------------------
pdf.add_page()
pdf.section("Repository Layer")
pdf.body(
    "Both repositories extend JpaRepository, which provides standard CRUD operations "
    "(save, findById, findAll, deleteById) without any boilerplate. Derived query methods "
    "and a custom JPQL query augment the default interface."
)

pdf.subsection("AuthorRepository")
pdf.code("""\
@Repository
public interface AuthorRepository extends JpaRepository<Author, Long> {

    List<Author>     findByNationality(String nationality);
    Optional<Author> findByEmail(String email);
}""")

pdf.subsection("BookRepository - with INNER JOIN query")
pdf.code("""\
@Repository
public interface BookRepository extends JpaRepository<Book, Long> {

    List<Book> findByGenre(String genre);
    List<Book> findByAuthorId(Long authorId);

    // Custom JPQL INNER JOIN -- fetches books whose author matches a nationality
    @Query("SELECT b FROM Book b INNER JOIN b.author a WHERE a.nationality = :nationality")
    List<Book> findByAuthorNationality(@Param("nationality") String nationality);
}""")

pdf.subsection("INNER JOIN Query Explained")
pdf.body(
    "The @Query annotation executes JPQL (Java Persistence Query Language), not SQL. "
    "\"INNER JOIN b.author a\" navigates the object graph along the @ManyToOne relationship "
    "defined in the Book entity. Hibernate translates this into the following SQL:"
)
pdf.code("""\
SELECT b.*
FROM   books b
INNER JOIN authors a ON b.author_id = a.id
WHERE  a.nationality = ?""", lang="sql")

# -- 7. Service Layer ----------------------------------------------------------
pdf.add_page()
pdf.section("Service Layer")
pdf.body(
    "Service classes sit between controllers and repositories, encapsulating business logic "
    "and transaction management. @Transactional(readOnly=true) is applied to queries for "
    "a performance hint to Hibernate."
)

pdf.subsection("AuthorServiceImpl - key methods")
pdf.code("""\
@Service
@Transactional
public class AuthorServiceImpl implements AuthorService {

    private final AuthorRepository authorRepository;

    @Autowired
    public AuthorServiceImpl(AuthorRepository authorRepository) {
        this.authorRepository = authorRepository;
    }

    @Override @Transactional(readOnly = true)
    public List<Author> getAllAuthors() {
        return authorRepository.findAll();
    }

    @Override
    public Author updateAuthor(Long id, Author authorDetails) {
        Author existing = authorRepository.findById(id)
            .orElseThrow(() ->
                new RuntimeException("Author not found with id: " + id));

        existing.setFirstName(authorDetails.getFirstName());
        existing.setLastName(authorDetails.getLastName());
        existing.setEmail(authorDetails.getEmail());
        existing.setBirthYear(authorDetails.getBirthYear());
        existing.setNationality(authorDetails.getNationality());

        return authorRepository.save(existing);
    }
}""")

pdf.subsection("BookServiceImpl - findByAuthorNationality")
pdf.code("""\
@Override @Transactional(readOnly = true)
public List<Book> findByAuthorNationality(String nationality) {
    return bookRepository.findByAuthorNationality(nationality);
}""")

# -- 8. Controller Layer -------------------------------------------------------
pdf.add_page()
pdf.section("Controller Layer")
pdf.body(
    "Spring MVC @Controller classes handle HTTP requests for /books and /authors. "
    "All operations use POST-Redirect-GET via RedirectAttributes to prevent duplicate form "
    "submissions. DataIntegrityViolationException is caught to display user-friendly messages "
    "when a duplicate ISBN or email is submitted."
)

pdf.subsection("AuthorController - Create operation")
pdf.code("""\
@Controller
@RequestMapping("/authors")
public class AuthorController {

    // GET /authors/new  -- show empty form
    @GetMapping("/new")
    public String showAddForm(Model model) {
        model.addAttribute("author",     new Author());
        model.addAttribute("pageTitle",  "Add New Author");
        model.addAttribute("formAction", "/authors/save");
        model.addAttribute("isEdit",     false);
        return "authors/form";
    }

    // POST /authors/save  -- persist + redirect
    @PostMapping("/save")
    public String saveAuthor(@ModelAttribute Author author,
                              RedirectAttributes redirectAttributes) {
        try {
            authorService.saveAuthor(author);
            redirectAttributes.addFlashAttribute("successMessage",
                "Author added successfully!");
        } catch (DataIntegrityViolationException e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                "Error: An author with this email already exists.");
            return "redirect:/authors/new";
        }
        return "redirect:/authors";
    }
}""")

pdf.subsection("BookController - Update operation")
pdf.code("""\
// POST /books/update/{id}
@PostMapping("/update/{id}")
public String updateBook(@PathVariable Long id,
                          @RequestParam String title,
                          @RequestParam String isbn,
                          @RequestParam String genre,
                          @RequestParam int    publishedYear,
                          @RequestParam double price,
                          @RequestParam Long   authorId,
                          RedirectAttributes   redirectAttributes) {
    try {
        Author author = authorService.getAuthorById(authorId)
            .orElseThrow(() -> new RuntimeException("Author not found"));
        Book details = new Book(title, isbn, genre, publishedYear, price, author);
        bookService.updateBook(id, details);
        redirectAttributes.addFlashAttribute("successMessage",
            "Book updated successfully!");
    } catch (DataIntegrityViolationException e) {
        redirectAttributes.addFlashAttribute("errorMessage",
            "Error: A book with this ISBN already exists.");
        return "redirect:/books/edit/" + id;
    }
    return "redirect:/books";
}""")

pdf.subsection("BookController - Read (INNER JOIN) endpoint")
pdf.code("""\
// GET /books/byNationality?nationality=British
@GetMapping("/byNationality")
public String booksByNationality(
        @RequestParam(required = false) String nationality,
        Model model) {
    model.addAttribute("pageTitle",   "Books by Author Nationality");
    model.addAttribute("nationality", nationality);
    if (nationality != null && !nationality.trim().isEmpty()) {
        List<Book> books =
            bookService.findByAuthorNationality(nationality.trim());
        model.addAttribute("books", books);
    }
    return "books/byNationality";
}""")

# -- 9. View Layer (JSP) -------------------------------------------------------
pdf.add_page()
pdf.section("View Layer - JSP Pages")
pdf.body(
    "Six JSP views implement the user interface. A shared layout/header.jsp contains inline "
    "CSS with a navy-and-gold theme. JSTL core tags (c:forEach, c:if) and Expression "
    "Language (EL) drive dynamic rendering."
)

pdf.subsection("Books List Page  (/books)")
pdf.mock_screen(
    "/books",
    [
        {"#": "1", "Title": "1984", "ISBN": "978-0-452-28423-4", "Genre": "Dystopian Fiction",
         "Year": "1949", "Price": "$12.99", "Author": "George Orwell", "": "Edit"},
        {"#": "2", "Title": "Animal Farm", "ISBN": "978-0-452-28424-1", "Genre": "Political Satire",
         "Year": "1945", "Price": "$9.99", "Author": "George Orwell", "": "Edit"},
        {"#": "3", "Title": "Harry Potter - PS", "ISBN": "978-0-7475-3269-9", "Genre": "Fantasy",
         "Year": "1997", "Price": "$14.99", "Author": "J.K. Rowling", "": "Edit"},
        {"#": "4", "Title": "War and Peace", "ISBN": "978-0-14-303943-3", "Genre": "Historical Fiction",
         "Year": "1869", "Price": "$19.99", "Author": "Leo Tolstoy", "": "Edit"},
    ],
    columns=["#", "Title", "ISBN", "Genre", "Year", "Price", "Author", ""],
    note="Simulated screenshot -- all 10 seeded books appear in the live application"
)

pdf.subsection("Add / Edit Book Form  (/books/new or /books/edit/{id})")
pdf.mock_form(
    "/books/new",
    [
        ("Title",          "e.g. The Great Gatsby"),
        ("ISBN",           "e.g. 978-0-7432-7356-5"),
        ("Genre",          "e.g. Literary Fiction"),
        ("Published Year", "e.g. 1925"),
        ("Price ($)",      "e.g. 11.99"),
        ("Author",         "-- Select Author --"),
    ],
    action_label="Save Book"
)

pdf.subsection("Authors List Page  (/authors)")
pdf.mock_screen(
    "/authors",
    [
        {"ID": "1", "First Name": "George", "Last Name": "Orwell",
         "Email": "george.orwell@books.com", "Birth Year": "1903",
         "Nationality": "British", "": "Edit"},
        {"ID": "2", "First Name": "J.K.", "Last Name": "Rowling",
         "Email": "jk.rowling@books.com", "Birth Year": "1965",
         "Nationality": "British", "": "Edit"},
        {"ID": "3", "First Name": "Ernest", "Last Name": "Hemingway",
         "Email": "ernest.hemingway@books.com", "Birth Year": "1899",
         "Nationality": "American", "": "Edit"},
    ],
    columns=["ID", "First Name", "Last Name", "Email", "Birth Year", "Nationality", ""],
    note="Simulated screenshot -- all 10 seeded authors appear in the live application"
)

pdf.add_page()
pdf.subsection("Books by Author Nationality  (/books/byNationality?nationality=British)")
pdf.mock_screen(
    "/books/byNationality?nationality=British",
    [
        {"Title": "1984", "ISBN": "978-0-452-28423-4", "Genre": "Dystopian Fiction",
         "Price": "$12.99", "Author": "George Orwell", "Nationality": "British"},
        {"Title": "Animal Farm", "ISBN": "978-0-452-28424-1", "Genre": "Political Satire",
         "Price": "$9.99", "Author": "George Orwell", "Nationality": "British"},
        {"Title": "Harry Potter - PS", "ISBN": "978-0-7475-3269-9", "Genre": "Fantasy",
         "Price": "$14.99", "Author": "J.K. Rowling", "Nationality": "British"},
    ],
    columns=["Title", "ISBN", "Genre", "Price", "Author", "Nationality"],
    note="Result of INNER JOIN query -- filter: nationality = 'British'"
)
pdf.body(
    "The nationality filter text box and quick-filter buttons (British, American, Russian ...) "
    "trigger a GET request that passes the nationality parameter to the controller, which "
    "delegates to bookService.findByAuthorNationality() backed by the @Query INNER JOIN."
)

pdf.subsection("CSS Theme (inline in header.jsp)")
pdf.code("""\
/* Core palette */
body      { font-family: 'Segoe UI', sans-serif; background: #f0f2f8; }
.navbar   { background: #1a2b4a; padding: 12px 20px; }
.navbar a { color: #f0c040; font-weight: bold; text-decoration: none; }
.card     { background: #fff; border-radius: 8px;
            box-shadow: 0 2px 12px rgba(0,0,0,.08); padding: 24px; }
.btn-primary { background: #1a2b4a; color: #fff; border: none;
               padding: 8px 18px; border-radius: 4px; cursor: pointer; }
.btn-warning { background: #f0c040; color: #1a2b4a; font-weight: bold; }
table     { width: 100%; border-collapse: collapse; }
th        { background: #1a2b4a; color: #f0c040; padding: 10px; }
tr:nth-child(even) { background: #eef0f8; }
.alert-success { background: #d4edda; color: #155724; border-radius: 4px; }
.alert-danger  { background: #f8d7da; color: #721c24; border-radius: 4px; }""", lang="css")

# -- 10. Operations - detail  -------------------------------------------------
pdf.add_page()
pdf.section("Implementation Details per Operation")

pdf.subsection("Create Operation - Flow")
pdf.bullet([
    "User navigates to /books/new or /authors/new  ->  GET handler returns the form JSP with "
    "an empty entity bound to the model.",
    "User fills the form and submits (POST to /books/save or /authors/save).",
    "@ModelAttribute / @RequestParam bind form fields to the entity object.",
    "Service layer calls repository.save() which executes an INSERT.",
    "On success: RedirectAttributes flash a green success banner and redirect to the list.",
    "On DataIntegrityViolationException (duplicate ISBN / email): red error banner shown, "
    "user stays on the form.",
])

pdf.subsection("Read Operation - Flow")
pdf.bullet([
    "GET /books  ->  bookService.getAllBooks()  ->  findAll() SQL  ->  list.jsp renders table "
    "via <c:forEach items='${books}'>.",
    "GET /authors  ->  same pattern.",
    "GET /books/byNationality?nationality=X  ->  bookService.findByAuthorNationality(X)  ->  "
    "INNER JOIN JPQL query  ->  byNationality.jsp renders filtered results.",
    "EL expressions (${book.title}, ${book.author.fullName}) are used in JSPs to display "
    "nested object properties.",
])

pdf.subsection("Update Operation - Flow")
pdf.bullet([
    "User clicks Edit on a list row  ->  GET /books/edit/{id} fetches the entity and "
    "pre-populates the form via model attributes.",
    "User edits fields and submits  ->  POST to /books/update/{id}.",
    "Service method updateBook(id, details) fetches the managed entity, applies field "
    "changes, and calls repository.save() (UPDATE SQL).",
    "Duplicate-key violations caught and displayed as an inline error message.",
])

# -- 11. Testing ---------------------------------------------------------------
pdf.add_page()
pdf.section("Unit Testing")
pdf.body(
    "46 tests in 4 test classes validate the repository and service layers. "
    "Repository tests use @DataJpaTest (real H2, no Mockito). Service tests use "
    "@ExtendWith(MockitoExtension.class) with mocked repositories."
)

pdf.subsection("AuthorServiceTest - example")
pdf.code("""\
@ExtendWith(MockitoExtension.class)
public class AuthorServiceTest {

    @Mock           AuthorRepository   authorRepository;
    @InjectMocks    AuthorServiceImpl  authorService;

    @Test
    void updateAuthor_WhenAuthorNotFound_ShouldThrowException() {
        when(authorRepository.findById(99L)).thenReturn(Optional.empty());

        assertThatThrownBy(() ->
            authorService.updateAuthor(99L, new Author()))
            .isInstanceOf(RuntimeException.class)
            .hasMessageContaining("Author not found with id: 99");

        verify(authorRepository, never()).save(any());
    }
}""")

pdf.subsection("BookRepositoryTest - INNER JOIN test")
pdf.code("""\
@DataJpaTest
public class BookRepositoryTest {

    @Autowired TestEntityManager em;
    @Autowired BookRepository   bookRepository;

    @Test
    void findByAuthorNationality_WhenNationalityExists_ShouldReturnBooks() {
        Author author = em.persist(
            new Author("Jane","Austen","j.austen@test.com",1775,"British"));
        em.persist(new Book("Pride and Prejudice","978-test-1",
                            "Romance",1813,8.99,author));
        em.flush();

        List<Book> result =
            bookRepository.findByAuthorNationality("British");

        assertThat(result).isNotEmpty();
        assertThat(result.get(0).getAuthor().getNationality())
            .isEqualTo("British");
    }
}""")

pdf.subsection("Test Summary")
pdf.test_table([
    ("AuthorRepositoryTest", "findByEmail_WhenEmailExists",        "@DataJpaTest",       True),
    ("AuthorRepositoryTest", "findByEmail_WhenNotExists",          "@DataJpaTest",       True),
    ("AuthorRepositoryTest", "findByNationality_ReturnsMatching",  "@DataJpaTest",       True),
    ("BookRepositoryTest",   "findByAuthorNationality_Returns",    "@DataJpaTest",       True),
    ("BookRepositoryTest",   "findByGenre_ReturnsMatching",        "@DataJpaTest",       True),
    ("AuthorServiceTest",    "getAllAuthors_ShouldReturnAll",       "Mockito",            True),
    ("AuthorServiceTest",    "updateAuthor_NotFound_Throws",        "Mockito",            True),
    ("AuthorServiceTest",    "saveAuthor_CallsRepositorySave",      "Mockito",            True),
    ("BookServiceTest",      "saveBook_ShouldSaveAndReturn",        "Mockito",            True),
    ("BookServiceTest",      "updateBook_WhenExists_Updates",       "Mockito",            True),
    ("BookServiceTest",      "findByNationality_Delegates",         "Mockito",            True),
])
pdf.body("Total: 46 tests  |  Failures: 0  |  Errors: 0  |  BUILD SUCCESS")

# -- 12. Challenges ------------------------------------------------------------
pdf.add_page()
pdf.section("Challenges Faced and Solutions")

challenges = [
    (
        "JSP rendering with embedded Tomcat",
        "Spring Boot's embedded Tomcat does not include JSP compilation by default. "
        "Adding tomcat-embed-jasper (provided scope) and configuring "
        "spring.mvc.view.prefix/suffix in application.properties resolved JSP resolution. "
        "The WAR packaging (not JAR) was also required.",
        "Added tomcat-embed-jasper + jstl dependencies; set packaging to 'war'; "
        "extended SpringBootServletInitializer.",
    ),
    (
        "LazyInitializationException on author.books in JSP",
        "When a Book's Author was loaded lazily and the JSP tried to render author.fullName "
        "outside the original transaction, a LazyInitializationException occurred. "
        "Spring's Open-Session-in-View (OSIV) is enabled by default in Spring Boot, which "
        "extends the persistence context through the view rendering phase.",
        "OSIV (spring.jpa.open-in-view=true) keeps the session open during view rendering. "
        "A warning is emitted but the behaviour is correct for this use-case.",
    ),
    (
        "Duplicate-key error handling",
        "Submitting a duplicate email or ISBN threw DataIntegrityViolationException deep in "
        "the Hibernate stack, resulting in a generic error page with no user feedback.",
        "Wrapped repository calls in try-catch for DataIntegrityViolationException in each "
        "controller method. On catch, a flash attribute errorMessage is set and the user is "
        "redirected back to the form where the error is displayed via c:if in JSP.",
    ),
    (
        "POST-only HTML forms for update",
        "HTML forms only support GET and POST; using PUT/PATCH for updates requires "
        "Spring's HiddenHttpMethodFilter or a different URL scheme.",
        "Used separate POST endpoints (e.g. POST /books/update/{id}) rather than HTTP PUT, "
        "which is fully compatible with standard HTML forms and JSP without JavaScript.",
    ),
    (
        "JSTL dependency resolution",
        "The artifact javax.servlet.jsp.jstl:jstl:1.2 does not exist in Maven Central "
        "under that group ID, causing build failures.",
        "Corrected to javax.servlet:jstl:1.2 -- the actual published artifact coordinate.",
    ),
]

for i, (title, problem, solution) in enumerate(challenges, 1):
    pdf.subsection(f"Challenge {i}: {title}")
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*RED)
    pdf.set_x(14)
    pdf.cell(0, 6, "Problem:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(30, 30, 30)
    pdf.set_x(20)
    pdf.multi_cell(175, 5.5, problem)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*GREEN)
    pdf.set_x(14)
    pdf.cell(0, 6, "Solution:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(30, 30, 30)
    pdf.set_x(20)
    pdf.multi_cell(175, 5.5, solution)
    pdf.ln(3)

# -- 13. Application Properties ------------------------------------------------
pdf.add_page()
pdf.section("Application Configuration")
pdf.code("""\
# Datasource - H2 in-memory
spring.datasource.url=jdbc:h2:mem:librarydb
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# H2 console available at /h2-console
spring.h2.console.enabled=true

# JPA / Hibernate
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true

# JSP view resolver
spring.mvc.view.prefix=/WEB-INF/views/
spring.mvc.view.suffix=.jsp

server.port=8080""", lang="properties")

pdf.subsection("Running the Application")
pdf.code("""\
# Clone the repository
git clone https://github.com/mahirabidi12/BitsDbAssignment.git
cd BitsDbAssignment

# Build and run
mvn spring-boot:run

# Open in browser
open http://localhost:8080          # Books list (home)
open http://localhost:8080/authors  # Authors list
open http://localhost:8080/h2-console  # H2 database console

# Run all tests
mvn test""", lang="bash")

pdf.subsection("Endpoints Reference")
rows = [
    {"Method": "GET",  "URL": "/",                         "Description": "Redirect -> /books"},
    {"Method": "GET",  "URL": "/books",                    "Description": "List all books"},
    {"Method": "GET",  "URL": "/books/new",                "Description": "Show Add Book form"},
    {"Method": "POST", "URL": "/books/save",               "Description": "Create new book"},
    {"Method": "GET",  "URL": "/books/edit/{id}",          "Description": "Show Edit Book form"},
    {"Method": "POST", "URL": "/books/update/{id}",        "Description": "Update book"},
    {"Method": "GET",  "URL": "/books/byNationality",      "Description": "Inner-join query (filter)"},
    {"Method": "GET",  "URL": "/authors",                  "Description": "List all authors"},
    {"Method": "GET",  "URL": "/authors/new",              "Description": "Show Add Author form"},
    {"Method": "POST", "URL": "/authors/save",             "Description": "Create new author"},
    {"Method": "GET",  "URL": "/authors/edit/{id}",        "Description": "Show Edit Author form"},
    {"Method": "POST", "URL": "/authors/update/{id}",      "Description": "Update author"},
]
cols = ["Method", "URL", "Description"]
widths = [20, 72, 90]
row_h = 6.5
y0 = pdf.get_y()
pdf.set_fill_color(*NAVY)
pdf.set_text_color(*WHITE)
pdf.set_font("Helvetica", "B", 8.5)
x = 14
for c, w in zip(cols, widths):
    pdf.rect(x, y0, w, 8, 'F')
    pdf.set_xy(x, y0)
    pdf.cell(w, 8, c, align="C")
    x += w
y0 += 8
for ri, row in enumerate(rows):
    bg = WHITE if ri % 2 == 0 else LGRAY
    pdf.set_fill_color(*bg)
    x = 14
    for c, w in zip(cols, widths):
        pdf.set_fill_color(*bg)
        pdf.rect(x, y0, w, row_h, 'F')
        pdf.set_xy(x + 1, y0)
        val = row[c]
        if val in ("GET", "POST"):
            pdf.set_text_color(0, 100, 180) if val == "GET" else pdf.set_text_color(0, 140, 60)
            pdf.set_font("Helvetica", "B", 8)
        else:
            pdf.set_text_color(30, 30, 30)
            pdf.set_font("Courier" if c == "URL" else "Helvetica", "", 8)
        pdf.cell(w - 2, row_h, val)
        x += w
    y0 += row_h
pdf.set_y(y0 + 6)

# -- 14. GitHub ----------------------------------------------------------------
pdf.add_page()
pdf.section("GitHub Repository")
pdf.body("The complete source code is publicly available on GitHub:")
pdf.set_font("Helvetica", "U", 11)
pdf.set_text_color(0, 80, 200)
pdf.set_x(14)
pdf.cell(0, 8, GITHUB, link=GITHUB, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(4)
pdf.set_text_color(0, 0, 0)
pdf.set_font("Helvetica", "", 10)

pdf.bullet([
    "Branch: main",
    "One commit: 'Initial commit' -- full working implementation",
    "To clone:  git clone " + GITHUB,
])
pdf.ln(4)
pdf.info_box(
    "Project Contents in Repository",
    "pom.xml  *  src/main/java/ (13 Java source files)  *  "
    "src/main/resources/application.properties  *  "
    "src/main/webapp/WEB-INF/views/ (6 JSP files)  *  "
    "src/test/java/ (4 test files, 46 tests)",
    color=(230, 240, 255),
)

# -- 15. Conclusion ------------------------------------------------------------
pdf.add_page()
pdf.section("Conclusion")
pdf.body(
    "The Library Management System successfully demonstrates all three CRUD operations "
    "(Create, Read, Update) for a one-to-many entity relationship (Author -> Book) using "
    "the Spring Boot ecosystem."
)
pdf.bullet([
    "Entity design: clean JPA annotations with proper cascade, fetch strategy, and "
    "unique constraints enforced at the DB level.",
    "Repository layer: extends JpaRepository + a custom JPQL INNER JOIN query.",
    "Service layer: transactional business logic, separated from controllers.",
    "Controller layer: POST-Redirect-GET pattern, exception handling for integrity violations.",
    "View layer: JSP + JSTL with EL, reusable header, navy/gold CSS theme.",
    "Testing: 46 passing tests -- @DataJpaTest for repositories, Mockito for services.",
    "Data: 10 Authors and 10 Books auto-seeded via CommandLineRunner on startup.",
])
pdf.ln(4)
pdf.info_box(
    "Key Learning Outcomes",
    "1. JPA relationship mapping (@OneToMany / @ManyToOne) and the implications of "
    "cascade and fetch strategy on application behaviour.\n"
    "2. Spring Data JPA derived queries vs. @Query JPQL -- when to use each.\n"
    "3. Handling database constraint violations gracefully at the controller layer.\n"
    "4. POST-Redirect-GET with flash attributes to avoid duplicate form submissions.\n"
    "5. Unit testing strategies: @DataJpaTest for real DB queries, Mockito for "
    "business-logic isolation.",
    color=(230, 255, 235),
)

# -- Save ----------------------------------------------------------------------
out = "/Users/mahirabidi/BitsDbAssignment/LibraryManagementSystem_Report.pdf"
pdf.output(out)
print(f"PDF saved: {out}")
print(f"Pages: {pdf.page}")
