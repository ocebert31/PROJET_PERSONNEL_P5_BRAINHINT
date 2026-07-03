import { ComponentFixture, TestBed } from '@angular/core/testing';
import { provideNoopAnimations } from '@angular/platform-browser/animations';

import { HomeComponent } from './home.component';

describe('HomeComponent', () => {
  let component: HomeComponent;
  let fixture: ComponentFixture<HomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HomeComponent],
      providers: [provideNoopAnimations()],
    }).compileComponents();

    fixture = TestBed.createComponent(HomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should invalidate an empty form', () => {
    expect(component.contactForm.invalid).toBeTrue();
  });

  it('should validate a complete form', () => {
    component.contactForm.setValue({
      name: 'Bertrand',
      email: 'bertrand@example.com',
      message: 'Hello BrainHint!',
    });

    expect(component.contactForm.valid).toBeTrue();
  });

  it('should store submitted values when form is valid', () => {
    component.contactForm.setValue({
      name: 'Bertrand',
      email: 'bertrand@example.com',
      message: 'Hello BrainHint!',
    });

    component.onSubmit();

    expect(component.submittedValue).toEqual({
      name: 'Bertrand',
      email: 'bertrand@example.com',
      message: 'Hello BrainHint!',
    });
  });

  it('should not submit when form is invalid', () => {
    component.onSubmit();

    expect(component.submittedValue).toBeNull();
  });

  it('should reset the form', () => {
    component.contactForm.setValue({
      name: 'Bertrand',
      email: 'bertrand@example.com',
      message: 'Hello BrainHint!',
    });
    component.onSubmit();

    component.resetForm();

    expect(component.contactForm.value).toEqual({
      name: '',
      email: '',
      message: '',
    });
    expect(component.submittedValue).toBeNull();
  });
});
