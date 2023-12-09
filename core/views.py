from django.shortcuts import render
from .models import Book, Author, Profile, Tag, Review
from django.db.models import Q, Count

def query_examples(request):
    authors = Author.objects.all()
    selected_author = authors[0]
    
    tags = Tag.objects.all()
    selected_tag = tags[0]
    
    books_by_author_name = Book.objects.filter(author__name=selected_author.name)
    books_by_tag_name = Book.objects.filter(tags__name=selected_tag)
    books_by_rating_gt_than_four = Book.objects.filter(
        Q(reviews__rating__gte=4) 
    )
    books_without_rating = Book.objects.filter(
        Q(reviews__isnull=True)
    )
    books_with_big_summary = Book.objects.filter(summary__gt=150)
    books_with_multiple_tags = Book.objects.annotate(tag_count=Count('tags')).filter(tag_count__gt=1)
    
    authors_by_keyword = Author.objects.filter(bio__icontains='amet')
    authors_greater_books_count = Author.objects.annotate(book_count=Count('books')).order_by('-book_count')
       
    profiles_with_specific_website = Profile.objects.filter(
        Q(website__icontains='silveira')
    )
    
    reviews_for_specific_author = Review.objects.filter(
        Q(book__author__name__icontains=authors[0].name)
    )
    

    # Envie todas as consultas para o template
    context = {
        'books_by_author_name': books_by_author_name,
        'books_by_tag_name': books_by_tag_name,
        'books_by_rating_gt_than_four': books_by_rating_gt_than_four,
        'books_without_rating': books_without_rating,
        'books_with_big_summary': books_with_big_summary,
        'books_with_multiple_tags': books_with_multiple_tags,
        
        'authors_by_keyword': authors_by_keyword,
        'authors_greater_books_count': authors_greater_books_count,
        
        'profiles_with_specific_website': profiles_with_specific_website,
        
        'reviews_for_specific_author': reviews_for_specific_author,
        
        'selected_tag': selected_tag,
        'selected_author': selected_author,
    }

    return render(request, 'core/teste1.html', context)
