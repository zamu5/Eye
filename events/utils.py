def get_request(session_id, category, since, until):
    params = {}
    if session_id:
        params['session_id'] = session_id
    if category:
        params['category'] = category
    if since and until:
        params['timestamp__gte'] = since
        params['timestamp__lte'] = until
    return params
