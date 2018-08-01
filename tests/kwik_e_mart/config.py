NLP_CONFIG = {
    'resolve_entities_using_nbest_transcripts': ['store_info.get_store_hours']
}

DEFAULT_ENTITY_RECOGNIZER_CONFIG = {
    'model_type': 'tagger',
    'label_type': 'entities',
    'model_settings': {
        'classifier_type': 'memm',
        'tag_scheme': 'IOB',
        'feature_scaler': 'max-abs'
    },
    'param_selection': {
        'type': 'k-fold',
        'k': 5,
        'scoring': 'accuracy',
        'grid': {
            'penalty': ['l1', 'l2'],
            'C': [0.01, 1, 100, 10000, 1000000, 100000000]
        },
    },
    'features': {
        'bag-of-words-seq': {
            'ngram_lengths_to_start_positions': {
                1: [-2, -1, 0, 1, 2],
                2: [-2, -1, 0, 1]
            }
        },
        'in-gaz-span-seq': {},
        'sys-candidates-seq': {
            'start_positions': [-1, 0, 1]
        }
    }
}


TEST_ENTITY_RECOGNIZER_CONFIG = {
    'model_type': 'tagger',
    'label_type': 'entities',
    'model_settings': {
        'classifier_type': 'memm',
        'tag_scheme': 'IOB',
        'feature_scaler': 'max-abs'
    },
    'param_selection': {
        'type': 'k-fold',
        'k': 5,
        'scoring': 'accuracy',
        'grid': {
            'penalty': ['l1', 'l2'],
            'C': [0.01, 1, 100, 10000, 1000000, 100000000]
        },
    },
    'features': {
        'bag-of-words-seq': {
            'ngram_lengths_to_start_positions': {
                1: [-2, -1, 0, 1, 2],
                2: [-2, -1, 0, 1]
            }
        },
        'in-gaz-span-seq': {},
        'sys-candidates-seq': {
            'start_positions': [-1, 0, 1]
        }
    },
    'train_label_set': 'testtrain.*\.txt',
    'test_label_set': 'testtrain.*\.txt'
}


def get_entity_recognizer_config(domain, intent):
    if domain == 'store_info' and intent == 'get_store_hours':
        return TEST_ENTITY_RECOGNIZER_CONFIG
    return DEFAULT_ENTITY_RECOGNIZER_CONFIG
