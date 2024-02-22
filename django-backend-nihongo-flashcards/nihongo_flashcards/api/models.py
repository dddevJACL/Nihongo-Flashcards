from django.db import models
from django.urls import reverse

# Create your models here.
class VocabularyCard(models.Model):
    """TODO"""
    
    # Fields for Vocabulary Card class
    vocab_word = models.CharField(max_length=25, help_text='Enter a vocabulary word for this flashcard')

    example_sentence = models.TextField(blank=True, help_text='Enter an example sentence for the vocabulary word')
    
    vocab_answer = models.TextField(help_text='Insert one or more definition(s), translation(s), etc. for your vocabulary word')

    num_times_correct = models.IntegerField(default=0)

    num_times_wrong = models.IntegerField(default=0)

    correct_streak = models.IntegerField(default=0)

    days_until_next_study = models.IntegerField(default=0, help_text='Enter an integer representing the number of days until you want to study this card again.')

    date_last_studied = models.DateTimeField(auto_now=True)
    
    # Metadata for Vocabulary Card class
    class Meta:
        ordering = ['-vocab_word']
    
    # Methods for Vocabulary Card class
    def get_absolute_url(self):
        """TODO"""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """TODO"""
        return self.vocab_word
