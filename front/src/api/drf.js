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
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
  },
	articles: {
    articles: () => HOST + ARTICLES,
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
    replies: commentPk => HOST + ARTICLES + `${commentPk}` + 'replies/',
    reply: (commentPk, replyPk) => HOST + ARTICLES + `${commentPk}` + 'replies/' + `${replyPk}`		
	}
}
