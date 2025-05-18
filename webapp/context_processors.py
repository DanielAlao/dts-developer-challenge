from django.urls import reverse
from django.conf import settings


def identity_context(request):
    authenticated = request.identity_context_data.authenticated
    claims = request.identity_context_data._id_token_claims
    # exclude_claims = ['iat', 'exp', 'nbf', 'uti', 'aio', 'rh']
    exclude_claims = ['iat', 'nbf', 'uti', 'aio', 'rh']
    claims_to_display = {claim: value for claim,
                         value in claims.items() if claim not in exclude_claims}

    return dict(authenticated=authenticated,
                claims_to_display=claims_to_display,
                redirect_uri_external_link=request.build_absolute_uri(reverse(settings.AAD_CONFIG.django.auth_endpoints.redirect)))
