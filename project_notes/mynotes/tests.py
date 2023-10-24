from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteTests(TestCase):
    #utilicé dichos y refranes populares para las pruebas, fueron nombras con el mismo nombre pero incremento para más práctico
    def setUp(self):
        self.nota1 = Note.objects.create(title='Nota Genial 1', content='Dime con quién andas y te diré quién eres.')
        self.nota2 = Note.objects.create(title='Nota Genial 2', content='El que mucho abarca, poco aprieta.')
        self.nota3 = Note.objects.create(title='Nota Genial 3', content='Más vale tarde que nunca.')
        self.nota4 = Note.objects.create(title='Nota Genial 4', content='Camarón que se duerme se lo lleva la corriente.')
        self.nota5 = Note.objects.create(title='Nota Genial 5', content='No hay mal que por bien no venga.')

    def test_note_creation(self):
        """Test las notas se crean correctamente."""
        self.assertEqual(self.nota1.title, 'Nota Genial 1')
        self.assertEqual(self.nota1.content, 'Dime con quién andas y te diré quién eres.')

    def test_note_list_view(self):
        """Test la lista de notas muestra las notas correctamente."""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dime con quién andas y te diré quién eres.')
        self.assertContains(response, 'No hay mal que por bien no venga.')

    def test_note_detail_view(self):
        """Test para la visualización detallada de la nota."""
        response = self.client.get(reverse('note_detail', args=(self.nota3.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Más vale tarde que nunca.')

    def test_note_update(self):
        """Test para la actualización de una nota."""
        updated_note = self.nota4
        updated_note.title = 'Nota Genial 4 (Editada)'
        updated_note.save()

        self.assertEqual(updated_note.title, 'Nota Genial 4 (Editada)')

    def test_note_deletion(self):
        """Test para eliminarr una nota."""
        note_count_before = Note.objects.count()
        self.nota5.delete()
        note_count_after = Note.objects.count()

        self.assertEqual(note_count_before - 1, note_count_after)
