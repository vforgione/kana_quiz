// chars is globalized from another script

/* global variables */
var correct_guesses = [],
    incorrect_guesses = []


/* helper functions */
function get_random_char() {
  // get a random index and get char
  var index = Math.floor(Math.random() * chars.length),
      char = chars[index]

  // remove char from array
  chars.splice(index, 1)

  // return char object
  console.log("plucked random char: " + JSON.stringify(char))
  console.log(chars.length + " chars remaining")
  return char
}


function render_quiz(char) {
  $('#current-char').text(char.char)
  $('#correct-answer').val(char.answer)
  $('#alternate-answer').val(char.alternate)
}


function check_answer() {
  // get elements and values
  var user_input = $('#user-input'),
      user_input_val = user_input.val().toLowerCase(),
      correct_answer = $('#correct-answer').val(),
      alternate_answer = $('#alternate-answer').val(),
      char = $('#current-char').text(),
      answer_tracker = $('#answer-tracker'),
      answer_tracker_html = answer_tracker.html()

  if (alternate_answer == '') { alternate_answer = undefined }

  console.log("user input: " + user_input_val)
  console.log("correct/alternate answers: " + correct_answer + "/" + alternate_answer)

  // clear user input
  user_input.val('')

  // test user input and update answer trackers
  if (user_input_val == correct_answer || user_input_val == alternate_answer) {
    correct_guesses.push(correct_answer)
    answer_tracker_html += '<span class="correct-answer">' + char + '</span>&nbsp;'
  } else {
    incorrect_guesses.push(correct_answer)
    answer_tracker_html += '<span class="incorrect-answer">' + char + '</span>&nbsp;'
  }
  answer_tracker.html(answer_tracker_html)

  // get new char
  try {
    var new_char = get_random_char()
    render_quiz(new_char)
  } catch (err) {
    console.log(err)
    if (err.message == "Cannot read property 'char' of undefined") {
      render_results()
    }
  }
}


function render_results() {
  console.log("correct guesses: " + correct_guesses)
  console.log("incorrect guesses: " + incorrect_guesses)

  // clear jumbotron
  $('#jumbotron').hide()

  // build results
  var answer_tracker = $('#answer-tracker'),
      answer_tracker_html = answer_tracker.html(),
      new_html = '<br /><br /><br />'
  if (incorrect_guesses.length) {
    var url = document.URL
    new_html += '<a class="btn btn-primary" href="' + url + '">Try Again</a>'
  } else {
    new_html += '<h3>Congratulations!</h3><p>You got all characters correct!</p>' +
        '<p>Go ahead and try another quiz!</p>'
  }

  // render
  answer_tracker.html(answer_tracker_html + new_html)
}


/* page load */
$(document).ready(function() {
  console.log(chars.length + " chars to start with")
  var char = get_random_char()
  render_quiz(char)
})
