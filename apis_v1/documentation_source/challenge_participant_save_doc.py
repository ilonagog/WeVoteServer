# apis_v1/documentation_source/challenge_participant_save_doc.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-


def challenge_participant_save_doc_template_values(url_root):
    """
    Show documentation about challengeParticipantSave
    """
    required_query_parameter_list = [
        {
            'name':         'voter_device_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'An 88 character unique identifier linked to a voter record on the server',
        },
        {
            'name':         'api_key',
            'value':        'string (from post, cookie, or get (in that order))',  # boolean, integer, long, string
            'description':  'The unique key provided to any organization using the WeVoteServer APIs',
        },
        {
            'name':         'challenge_we_vote_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The we_vote_id for the challenge.',
        },
        {
            'name':         'voter_we_vote_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The voter_we_vote_id for the supporter.',
        },
    ]
    optional_query_parameter_list = [
        {
            'name':         'organization_we_vote_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The organization_we_vote_id for the supporter.',
        },
        {
            'name':         'participant_name',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The title of the challenge.',
        },
        {
            'name':         'participant_name_changed',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'Are we trying to change the challenge\'s title?',
        },
        {
            'name': 'supporter_endorsement',
            'value': 'string',  # boolean, integer, long, string
            'description': 'The title of the challenge.',
        },
        {
            'name': 'supporter_endorsement_changed',
            'value': 'boolean',  # boolean, integer, long, string
            'description': 'Are we trying to change the challenge\'s title?',
        },
        {
            'name': 'visible_to_public',
            'value': 'string',  # boolean, integer, long, string
            'description': 'The title of the challenge.',
        },
        {
            'name': 'visible_to_public_changed',
            'value': 'boolean',  # boolean, integer, long, string
            'description': 'Are we trying to change the challenge\'s title?',
        },
    ]

    potential_status_codes_list = [
        {
            'code':         'VALID_VOTER_DEVICE_ID_MISSING',
            'description':  'Cannot proceed. A valid voter_device_id parameter was not included.',
        },
        {
            'code':         'VALID_VOTER_ID_MISSING',
            'description':  'Cannot proceed. A valid voter_id was not found.',
        },
    ]

    try_now_link_variables_dict = {
        # 'challenge_we_vote_id': 'wv85camp1',
    }

    api_response = '{\n' \
                   '  "status": string,\n' \
                   '  "success": boolean,\n' \
                   '  "challenge_we_vote_id": string,\n' \
                   '  "date_last_changed": string,\n' \
                   '  "date_joined": string,\n' \
                   '  "organization_we_vote_id": string,\n' \
                   '  "supporter_endorsement": string,\n' \
                   '  "participant_name": string,\n' \
                   '  "visible_to_public": boolean,\n' \
                   '  "voter_we_vote_id": string,\n' \
                   '  "we_vote_hosted_profile_image_url_tiny": string,\n' \
                   '}'

    template_values = {
        'api_name': 'challengeParticipantSave',
        'api_slug': 'challengeParticipantSave',
        'api_introduction':
            "",
        'try_now_link': 'apis_v1:challengeParticipantSaveView',
        'try_now_link_variables_dict': try_now_link_variables_dict,
        'url_root': url_root,
        'get_or_post': 'GET',
        'required_query_parameter_list': required_query_parameter_list,
        'optional_query_parameter_list': optional_query_parameter_list,
        'api_response': api_response,
        'api_response_notes':
            "",
        'potential_status_codes_list': potential_status_codes_list,
    }
    return template_values
