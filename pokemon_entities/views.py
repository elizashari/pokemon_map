import folium

from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.utils import timezone
from .models import PokemonEntity, Pokemon

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    current_time = timezone.localtime()

    pokemon_entities = PokemonEntity.objects.filter(disappear_at__gte=current_time,
                                                    appear_at__lte=current_time).select_related('pokemon')
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.long,
            request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.photo.url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    next_evolution = requested_pokemon.next_evolutions.first()

    pokemon = {
        "title_ru": requested_pokemon.title,
        "img_url": requested_pokemon.photo.url,
        "title_en": requested_pokemon.title_en,
        "title_jp": requested_pokemon.title_jp,
        "description": requested_pokemon.description,
        "previous_evolution": requested_pokemon.previous_evolution,
        "next_evolution": next_evolution
    }
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    current_time = timezone.localtime()
    requested_pokemon_entities = PokemonEntity.objects.filter(pokemon__id=pokemon_id, disappear_at__gte=current_time,
                                                              appear_at__lte=current_time)
    for pokemon_entity in requested_pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.long,
            request.build_absolute_uri(requested_pokemon.photo.url)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })