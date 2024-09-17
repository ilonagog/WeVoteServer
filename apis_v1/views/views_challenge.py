# apis_v1/views/views_challenge.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-
from challenge.controllers import challenge_list_retrieve_for_api, challenge_news_item_save_for_api, \
    challenge_retrieve_for_api, challenge_save_for_api, \
    challenge_participant_retrieve_for_api, challenge_participant_save_for_api
from config.base import get_environment_variable
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_user_agents.utils import get_user_agent
from exception.models import handle_exception
# from follow.controllers import voter_challenge_follow_for_api
import json
import wevote_functions.admin
from wevote_functions.functions import get_voter_device_id, positive_value_exists

logger = wevote_functions.admin.get_logger(__name__)

WE_VOTE_SERVER_ROOT_URL = get_environment_variable("WE_VOTE_SERVER_ROOT_URL")


def challenge_list_retrieve_view(request):  # challengeListRetrieve (No CDN)
    hostname = request.GET.get('hostname', '')
    limit_to_this_state_code = request.GET.get('state_code', '')
    recommended_challenges_for_challenge_we_vote_id = \
        request.GET.get('recommended_challenges_for_challenge_we_vote_id', '')
    search_text = request.GET.get('search_text', '')
    voter_device_id = get_voter_device_id(request)  # We standardize how we take in the voter_device_id
    json_data = challenge_list_retrieve_for_api(
        hostname=hostname,
        limit_to_this_state_code=limit_to_this_state_code,
        recommended_challenges_for_challenge_we_vote_id=recommended_challenges_for_challenge_we_vote_id,
        request=request,
        search_text=search_text,
        voter_device_id=voter_device_id,
    )
    json_string = ''
    try:
        json_string = json.dumps(json_data)
    except Exception as e:
        status = "Caught error for voter_device_id " + voter_device_id
        handle_exception(e, logger=logger, exception_message=status)

    return HttpResponse(json_string, content_type='application/json')


def challenge_news_item_save_view(request):  # challengeNewsItemSave
    voter_device_id = get_voter_device_id(request)  # We standardize how we take in the voter_device_id
    challenge_news_subject = request.GET.get('challenge_news_subject', '')
    challenge_news_subject_changed = positive_value_exists(request.GET.get('challenge_news_subject_changed', False))
    challenge_news_text = request.GET.get('challenge_news_text', '')
    challenge_news_text_changed = positive_value_exists(request.GET.get('challenge_news_text_changed', False))
    challenge_news_item_we_vote_id = request.GET.get('challenge_news_item_we_vote_id', '')
    challenge_we_vote_id = request.GET.get('challenge_we_vote_id', '')
    in_draft_mode = positive_value_exists(request.GET.get('in_draft_mode', False))
    in_draft_mode_changed = positive_value_exists(request.GET.get('in_draft_mode_changed', False))
    send_now = positive_value_exists(request.GET.get('send_now', False))
    visible_to_public = positive_value_exists(request.GET.get('visible_to_public', True))
    visible_to_public_changed = positive_value_exists(request.GET.get('visible_to_public_changed', False))
    json_data = challenge_news_item_save_for_api(
        challenge_news_subject=challenge_news_subject,
        challenge_news_subject_changed=challenge_news_subject_changed,
        challenge_news_text=challenge_news_text,
        challenge_news_text_changed=challenge_news_text_changed,
        challenge_news_item_we_vote_id=challenge_news_item_we_vote_id,
        challenge_we_vote_id=challenge_we_vote_id,
        in_draft_mode=in_draft_mode,
        in_draft_mode_changed=in_draft_mode_changed,
        send_now=send_now,
        visible_to_public=visible_to_public,
        visible_to_public_changed=visible_to_public_changed,
        voter_device_id=voter_device_id,
    )
    return HttpResponse(json.dumps(json_data), content_type='application/json')


def challenge_participant_retrieve_view(request):  # challengeParticipantRetrieve
    voter_device_id = get_voter_device_id(request)  # We standardize how we take in the voter_device_id
    challenge_we_vote_id = request.GET.get('challenge_we_vote_id', '')
    json_data = challenge_participant_retrieve_for_api(
        voter_device_id=voter_device_id,
        challenge_we_vote_id=challenge_we_vote_id,
    )
    return HttpResponse(json.dumps(json_data), content_type='application/json')


def challenge_retrieve_view(request):  # challengeRetrieve (CDN)
    voter_device_id = get_voter_device_id(request)  # We standardize how we take in the voter_device_id
    challenge_we_vote_id = request.GET.get('challenge_we_vote_id', '')
    hostname = request.GET.get('hostname', '')
    seo_friendly_path = request.GET.get('seo_friendly_path', '')
    json_data = challenge_retrieve_for_api(
        voter_device_id=voter_device_id,
        challenge_we_vote_id=challenge_we_vote_id,
        hostname=hostname,
        seo_friendly_path=seo_friendly_path,
    )
    return HttpResponse(json.dumps(json_data), content_type='application/json')


def challenge_retrieve_as_owner_view(request):  # challengeRetrieveAsOwner (No CDN)
    voter_device_id = get_voter_device_id(request)  # We standardize how we take in the voter_device_id
    challenge_we_vote_id = request.GET.get('challenge_we_vote_id', '')
    seo_friendly_path = request.GET.get('seo_friendly_path', '')
    hostname = request.GET.get('hostname', '')
    json_data = challenge_retrieve_for_api(
        voter_device_id=voter_device_id,
        challenge_we_vote_id=challenge_we_vote_id,
        as_owner=True,
        hostname=hostname,
        seo_friendly_path=seo_friendly_path,
    )
    return HttpResponse(json.dumps(json_data), content_type='application/json')


@csrf_exempt
def challenge_save_view(request):  # challengeSave & challengeStartSave
    # This is set in /config/base.py: DATA_UPLOAD_MAX_MEMORY_SIZE = 6000000
    voter_device_id = get_voter_device_id(request)  # We standardize how we take in the voter_device_id
    challenge_description = request.POST.get('challenge_description', '')
    challenge_description_changed = positive_value_exists(request.POST.get('challenge_description_changed', False))
    in_draft_mode = positive_value_exists(request.POST.get('in_draft_mode', True))
    in_draft_mode_changed = positive_value_exists(request.POST.get('in_draft_mode_changed', False))
    challenge_photo_from_file_reader = request.POST.get('challenge_photo_from_file_reader', '')
    challenge_photo_changed = positive_value_exists(request.POST.get('challenge_photo_changed', False))
    challenge_photo_delete = request.POST.get('challenge_photo_delete', '')
    challenge_photo_delete_changed = positive_value_exists(request.POST.get('challenge_photo_delete_changed', False))
    challenge_title = request.POST.get('challenge_title', '')
    challenge_title_changed = positive_value_exists(request.POST.get('challenge_title_changed', False))
    challenge_we_vote_id = request.POST.get('challenge_we_vote_id', '')
    hostname = request.POST.get('hostname', '')
    politician_delete_list_serialized = request.POST.get('politician_delete_list', '')
    politician_starter_list_serialized = request.POST.get('politician_starter_list', '')
    politician_starter_list_changed = positive_value_exists(request.POST.get('politician_starter_list_changed', False))
    json_data = challenge_save_for_api(
        challenge_description=challenge_description,
        challenge_description_changed=challenge_description_changed,
        in_draft_mode=in_draft_mode,
        in_draft_mode_changed=in_draft_mode_changed,
        challenge_photo_from_file_reader=challenge_photo_from_file_reader,
        challenge_photo_changed=challenge_photo_changed,
        challenge_photo_delete=challenge_photo_delete,
        challenge_photo_delete_changed=challenge_photo_delete_changed,
        challenge_title=challenge_title,
        challenge_title_changed=challenge_title_changed,
        challenge_we_vote_id=challenge_we_vote_id,
        hostname=hostname,
        politician_delete_list_serialized=politician_delete_list_serialized,
        politician_starter_list_serialized=politician_starter_list_serialized,
        politician_starter_list_changed=politician_starter_list_changed,
        request=request,
        voter_device_id=voter_device_id,
    )
    return HttpResponse(json.dumps(json_data), content_type='application/json')


def challenge_participant_save_view(request):  # challengeParticipantSave
    voter_device_id = get_voter_device_id(request)  # We standardize how we take in the voter_device_id
    visible_to_public = positive_value_exists(request.GET.get('visible_to_public', True))
    visible_to_public_changed = positive_value_exists(request.GET.get('visible_to_public_changed', False))
    challenge_we_vote_id = request.GET.get('challenge_we_vote_id', '')
    json_data = challenge_participant_save_for_api(
        challenge_we_vote_id=challenge_we_vote_id,
        visible_to_public=visible_to_public,
        visible_to_public_changed=visible_to_public_changed,
        voter_device_id=voter_device_id,
    )
    return HttpResponse(json.dumps(json_data), content_type='application/json')


def voter_challenge_follow_view(request):  # challengeFollow
    voter_device_id = get_voter_device_id(request)  # We standardize how we take in the voter_device_id
    issue_we_vote_id = request.GET.get('issue_we_vote_id', False)
    google_civic_election_id = request.GET.get('google_civic_election_id', 0)
    follow_value = positive_value_exists(request.GET.get('follow', False))
    user_agent_string = request.headers['user-agent']
    user_agent_object = get_user_agent(request)
    ignore_value = positive_value_exists(request.GET.get('ignore', False))

    # TODO
    result = {}
    # result = voter_challenge_follow_for_api(
    #     voter_device_id=voter_device_id,
    #     issue_we_vote_id=issue_we_vote_id,
    #     follow_value=follow_value,
    #     ignore_value=ignore_value, user_agent_string=user_agent_string,
    #     user_agent_object=user_agent_object)
    result['google_civic_election_id'] = google_civic_election_id
    return HttpResponse(json.dumps(result), content_type='application/json')
