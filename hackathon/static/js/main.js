function handleReplyButton(commentId) {
  const replyFormContainer = document.getElementById(`reply-form-container-${commentId}`);
  if (replyFormContainer) {
    replyFormContainer.className = 'reply-form-container enabled'
  }
}

function handleCancelReply(commentId) {
  const replyFormContainer = document.getElementById(`reply-form-container-${commentId}`);
  if (replyFormContainer) {
    replyFormContainer.className = 'reply-form-container'
  }
}