import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';
import { Book } from '../models/Book';
import { BookService } from '../book/book.service';
import { MatTableModule } from '@angular/material/table'
import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatInputModule } from '@angular/material/input'
import { MatFormFieldModule } from '@angular/material/form-field'
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatTableDataSource } from '@angular/material/table';
import { provideAnimations } from '@angular/platform-browser/animations';

@Component({
  selector: 'app-book-list',
  standalone: true,
  imports: [CommonModule, HttpClientModule,
    MatTableModule,
    MatCardModule,
    MatButtonModule,
    MatInputModule,
    MatFormFieldModule, ReactiveFormsModule,
  ],
  providers: [
    provideAnimations(),
  ],
  templateUrl: './book-list.component.html',
  styleUrl: './book-list.component.css'
})
export class BookListComponent implements OnInit {
  isadd = false;
  isedit = false;
  displayedColums: string[] = ['id', 'title', 'author', 'action']

  private bookService = inject(BookService);
  datasource: any;
  books: Book[] = [];
  book!: Book;


  constructor(private builder: FormBuilder) {
  }

  ngOnInit(): void {
    this.loadBooks();
    console.log(this.books);
  }


  loadBooks() {
    this.bookService.getBooks()
      .subscribe((data) => {
        this.books = data;
        this.datasource = new MatTableDataSource(this.books);
      })
  }


  bookForm = this.builder.group({
    id: this.builder.control({ value: 0, disabled: true }),
    title: this.builder.control('', Validators.required),
    author: this.builder.control('', Validators.required)
  })
  addBook() {
    if (this.bookForm.valid) {
      const _obj: Book = {
        id: this.bookForm.value.id as number,
        title: this.bookForm.value.title as string,
        author: this.bookForm.value.author as string,
      }
      if (this.isadd) {
        this.bookService.addBook(_obj).subscribe(item => {
          this.loadBooks();
          this.isadd = false;
          this.isedit = false;
          alert('Created successfully.')
        });
      } else {
        _obj.id = this.bookForm.getRawValue().id as number;
        this.bookService.editBook(_obj.id, _obj).subscribe(item => {
          this.loadBooks();
          this.isadd = false;
          this.isedit = false;
          alert('Updated successfully.')
        });
      }
    }
  }

  editproduct(id: number) {
    this.bookService.getBook(id).subscribe(item => {
      this.book = item;
      this.bookForm.setValue({ id: this.book.id, title: this.book.title, author: this.book.author });
      this.isedit = true;
    })
  }
  removeproduct(id: number) {
    if (confirm('Confirm to remove?')) {
      this.bookService.deleteBook(id).subscribe(item => {
        this.loadBooks();
      })
    }
  }


  openForm() {
    this.bookForm.reset();
    this.isadd = true;
    this.isedit = false;
  }
  backtolist() {
    this.isadd = false;
    this.isedit = false;
  }


}
