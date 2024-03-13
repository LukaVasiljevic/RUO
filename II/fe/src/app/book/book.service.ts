import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Book } from '../models/Book';

const BASE_URL = 'http://localhost:5000'
@Injectable({
  providedIn: 'root'
})
export class BookService {
  private httpClient = inject(HttpClient);

  constructor() { }

  getBooks() {
    return this.httpClient
      .get<Book[]>(BASE_URL + '/books');
  }

  getBook(id: number) {
    return this.httpClient
      .get<Book>(BASE_URL + '/books/' + id);
  }
  addBook(book: Book) {
    return this.httpClient
      .post<Book>(BASE_URL + '/books', book);
  }
  editBook(id: number, book: Book) {
    return this.httpClient
      .put<Book>(BASE_URL + '/books/' + id, book);
  }
  deleteBook(id: number) {
    return this.httpClient
      .delete(BASE_URL + '/books/' + id);
  }
}
