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
        'description TINYTEXT',
    ])

INSERT('products', {
    'name': 'Surfboard long',
    'category': 'surfboard',
    'slug': 'slong',
    'description': 'this is description for surfboard long',
})

INSERT('products', {
    'name': 'Surfboard Professional',
    'category': 'surfboard',
    'slug': 'sprofessional',
    'description': 'this is description for surfboard professional',
})

INSERT('products', {
    'name': 'Surfboard Artist Collection',
    'category': 'surfboard',
    'slug': 'sartistcollection',
    'description': 'this is description for surfboard artist collection',
})

INSERT('products', {
    'name': 'Climbing Shoes Men',
    'category': 'climbing',
    'slug': 'csmen',
    'description': 'this is description for climbing shoes men',
})

INSERT('products', {
    'name': 'Climbing Shoes Women',
    'category': 'climbing',
    'slug': 'cswomen',
    'description': 'this is description for climbing shoes women',
})

INSERT('products', {
    'name': 'Rock Climbing Shoes',
    'category': 'climbing',
    'slug': 'rockcs',
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
