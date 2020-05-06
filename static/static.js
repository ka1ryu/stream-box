document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach(el => {
      el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });
  }

});

// contact-form
function postFormToGoogle() {
  var name = $("#formName").val();
  var email = $("#formEmail").val();
  var subject = $("#formSubject").val();
  var mes = $("#formMessage").val();

  // Ajax通信を開始する
  $.ajax({
    type: "POST",
    url: 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSfTaZL6xd6UD-dUuBg6EAx_iL4XvifmsheYjZ8dl0DOyalyxg/formResponse',
    data: {
      "entry.2060346825": name,
      "emailAddress": email,
      "entry.1959976867": subject,
      "entry.2132256282": mes
    },
    dataType: "xml",
    success: function () {
      console.log('成功');
    },
    error: function () {
    }
  })
}

$(function () {
  $(".contact-form-button").on('click', function () {

    var nameFlag = "false";
    var emailFlag = "false";
    var mesFlag = "false";

    //check name
    if ($("#formName").val() == "") {
      $(".form-name-info").text("入力内容に不備があります。");
      $("#formName").addClass("is-danger");
    } else {
      $(".form-name-info").text("");
      $("#formName").removeClass("is-danger");
      nameFlag = "true";
    }

    //check email
    if (!$("#formEmail").val().match(/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/)) {
      $(".form-email-info").text("入力内容に不備があります。")
      $("#formEmail").addClass("is-danger");
    } else {
      $(".form-email-info").text("");
      $("#formEmail").removeClass("is-danger");
      emailFlag = "true";
    }

    //check mes
    if ($("#formMessage").val() == "") {
      $(".form-message-info").text("入力内容に不備があります")
      $("#formMessage").addClass("is-danger");
    } else {
      $(".form-message-info").text("");
      $("#formMessage").removeClass("is-danger");
      mesFlag = "true";
    }

    if (nameFlag == "true" && emailFlag == "true" && mesFlag == "true") {
      postFormToGoogle();
      $(".help").text("");
      $(".form-complete").text("送信完了しました。");
    }
  });
});