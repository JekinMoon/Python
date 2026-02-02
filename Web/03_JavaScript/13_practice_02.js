const form = document.querySelector('form');
const list = document.querySelector('.comment-list');

// form 요소의 button을 클릭하여 폼을 "제출"했을 때,
form.addEventListener('submit', function (e) {
  e.preventDefault(); // 폼이 제출되고 새로고침 되는 것을 막음

  const userid = document.querySelector('input[name="userid"]'); // userid 폼 요소에 접근하기
  const comment = document.querySelector('input[name="comment"]'); // comment 폼 요소에 접근하기
  // const userid = form.elements.userid;
  // const comment = form.elements.comment;

  const newComment = document.createElement('li'); // li 태그를 생성하기
  newComment.innerHTML = `<b>${userid.value}</b> - ${comment.value}`; // 태그 내용으로 "Id - comment" 를 적어주기
  list.append(newComment); // .comment-list 요소에 위에서 만든 li 태그 추가하기

  userid.value = ''; // userid 입력창 초기화
  comment.value = ''; // comment 입력창 초기화
});