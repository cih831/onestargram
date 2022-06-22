const HOST = 'http://127.0.0.1:8090/api/v1/'

const ARTICLES = 'articles/'
const ACCOUNTS = 'accounts/'
const COMMENTS = 'comments/'

export default { 
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
    follow: username => HOST + ACCOUNTS + 'profile/' + `${username}/` + 'follow/',
    edit: username => HOST + ACCOUNTS + 'profile/' + `${username}/` + 'edit/',
    editProfileImg: username => HOST + ACCOUNTS + 'profile/' + `${username}/` + 'edit_profile_img/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
  },
	articles: {
    articles: () => HOST + ARTICLES,
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    createComment: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    updateDeleteComment: commentPk => HOST + ARTICLES + COMMENTS + `${commentPk}/`,
    likeComment: commentPk => HOST + ARTICLES + COMMENTS + `${commentPk}/` + 'like/',
    createReply: commentPk => HOST + ARTICLES + COMMENTS + `${commentPk}/` + 'replies/',
    updateDeleteReply: (commentPk, replyPk) => HOST + ARTICLES + COMMENTS + `${commentPk}/` + 'replies/' `${replyPk}/`,
    likeReply: replyPk => HOST + ARTICLES + 'replies/' + `${replyPk}/` + 'like/',
	}
}
