from database import (
    DROP_TABLES,
    CREATE_TABLE,
    INSERT,
    SELECT,
    SELECT_WHERE,
)

DROP_TABLES('products')

CREATE_TABLE(
    'products',
    [
        'id INT AUTO_INCREMENT PRIMARY KEY',
        'name VARCHAR(255)',
        'category VARCHAR(255)',
        'slug VARCHAR(255)',
        'image_src VARCHAR(255)',
        'description TINYTEXT',
    ]
)

INSERT('products', {
    'name': 'Surfboard long',
    'category': 'surfboard',
    'slug': 'slong',
    'image_src': 'https://www.skidsport.nu/images/2.35320/nsp-longboard-elements-hdt-navy.jpeg',
    'description': 'this is description for surfboard long',
})

INSERT('products', {
    'name': 'Surfboard Professional',
    'category': 'surfboard',
    'slug': 'sprofessional',
    'image_src': 'https://cdn.newport.se/gallery/14912/webbild_fe121__fullsize.jpg',
    'description': 'this is description for surfboard professional',
})

INSERT('products', {
    'name': 'Surfboard Artist Collection',
    'category': 'surfboard',
    'slug': 'sartistcollection',
    'image_src': 'https://media.artsper.com/artwork/632721_1_m.jpg',
    'description': 'this is description for surfboard artist collection',
})

INSERT('products', {
    'name': 'Climbing Shoes Men',
    'category': 'climbing',
    'slug': 'csmen',
    'image_src': 'https://www.c2safety.com/wp-content/uploads/pyr/large/2/219df4a7-1c7e-4c50-ae40-b3e4922aaf56.jpg',
    'description': 'this is description for climbing shoes men',
})

INSERT('products', {
    'name': 'Climbing Shoes Women',
    'category': 'climbing',
    'slug': 'cswomen',
    'image_src': 'https://www.lasportiva.com/media/catalog/product/3/6/36Z_619620_04.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=700&width=700&canvas=700:700',
    'description': 'this is description for climbing shoes women',
})

INSERT('products', {
    'name': 'Rock Climbing Shoes',
    'category': 'climbing',
    'slug': 'rockcs',
    'image_src': 'https://www.bfgcdn.com/1500_1500_90/301-0107/la-sportiva-tc-pro-klaetterskor-detail-4.jpg',
    'description': 'this is description for rock climbing shoes',
})

print(
    '"climbing" Products : ',
    SELECT_WHERE(
        'products', [
            'id',
            'name',
            'category',
            'description',
        ],
        'category',
        'climbing'
    )
)
print('')
print(
    '"surfboard" Products : ',
    SELECT_WHERE(
        'products', [
            'id',
            'name',
            'category',
            'description',
        ],
        'category',
        'surfboard'
    )
)
