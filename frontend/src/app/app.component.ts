import { Component } from '@angular/core';
import { AppShellComponent } from './layout/app-shell/app-shell.component';

@Component({
  selector: 'app-root',
  imports: [AppShellComponent],
  template: '<app-app-shell />',
  styles: ':host { display: block; min-height: 100vh; }',
})
export class AppComponent {}
