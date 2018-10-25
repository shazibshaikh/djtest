from polls.models import Person
p = Person.objects.create(name='Horatio', post_nominals=['BSc', 'RA'])
p.post_nominals
#['PhD', 'Esq.']
p.post_nominals.append('I')
p.post_nominals
#['PhD', 'Esq.', 'III']
p.save()
Person.objects.all()