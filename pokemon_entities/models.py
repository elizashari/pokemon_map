from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField('Имя', max_length=200)
    title_en = models.CharField('Имя англ', max_length=200, blank=True)
    title_jp = models.CharField('Имя яп', max_length=200, blank=True)
    photo = models.ImageField('Изображение', upload_to='pokemon', null=True)
    description = models.TextField('Описание', null=True, blank=True)
    previous_evolution = models.ForeignKey('self', verbose_name='Эволюционировал из',
                                           null=True, blank=True,
                                           on_delete=models.SET_NULL,
                                           related_name='next_evolutions')
    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Имя', on_delete=models.PROTECT, related_name='entities')
    lat = models.FloatField('Широта')
    long = models.FloatField('Долгота')
    appear_at = models.DateTimeField('Время появления', null=True, blank=False)
    disappear_at = models.DateTimeField('Время исчезание', null=True, blank=False)
    level = models.FloatField('Уровень', blank=True)
    health = models.CharField('Здоровье', max_length=200, blank=True)
    attack = models.CharField('Атака', max_length=200, blank=True)
    defence = models.CharField('Защита', max_length=200, blank=True)
    stamina = models.CharField('Выносливость', max_length=200, blank=True)
    def __str__(self):
        return self.pokemon.title