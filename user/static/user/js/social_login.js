function buildQuery(params) {
    return Object.keys(params).map(function (key) {return key + '=' + encodeURIComponent(params[key])}).join('&')
}
function buildUrl(baseUrl, queries) {
    return baseUrl + '?' + buildQuery(queries)
}

function googleLogin() { // 구글 로그인 아직 미완
    params = {
        response_type: 'code',
        client_id:'',
        redirect_uri: location.origin + '/user/login/social/naver/callback/',
        state: document.querySelector('[name=csrfmiddlewaretoken]').value
    }
    "url = buildUrl('https://nid.naver.com/oauth2.0/authorize', params)"
    location.replace(url)
}