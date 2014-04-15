rights = [ 'Bingo!', 'Yes!', 'Correct', 'Nailed it', 'Right', 'You got it', 'Check', '+1', 'Affirmative'];
wrongs = [ 'Nope', 'Wrong', 'Miss', 'Missed it', 'Incorrect', 'Sorry'];
famous_adjs = [ 'acclaimed', 'brilliant', 'distinguished', 'eminent', 'excellent', 'glorious', 'grand', 'great', 'honored', 'illustrious', 'important', 'influential', 'leading', 'memorable', 'noted', 'notorious', 'outstanding', 'powerful', 'preeminent', 'prominent', 'recognized', 'remarkable', 'renowned', 'splendid', 'well-known', 'applauded', 'august', 'celebrated', 'conspicuous', 'elevated', 'exalted', 'extraordinary', 'foremost', 'imposing', 'lionized', 'mighty', 'publicized', 'noble', 'noteworthy', 'peerless', 'reputable', 'signal', 'talked-about'];
famous_nouns = [ 'figure', 'hero', 'luminary', 'personage', 'personality', 'someone', 'star', 'superstar', 'ace', 'bigwig', 'cynosure', 'heavyweight', 'hotshot', 'immortal', 'lion', 'magnate', 'mahatma', 'name', 'notable', 'somebody', 'VIP', 'worthy', 'big-cheese', 'big-shot', 'celeb', 'major-leaguer'];
potential_lists = [ "Disney princesses", "Characters in Harry Potter", "Greek gods and goddesses", "Presidents of the U.S.", "Nobel prize winners", "Current members of Congress", "Top 1,000 people on twitter", "Fortune 500 CEOs", "Who's who in Silicon Valley", "Famous criminals", "Famous authors", "Civil war generals", "People who making headlines this month", "Billionaires", "Tyrants", "Prominent botanists", "High-powered attorneys and judges", "Oscar winning actors and actresses", "Famous women", "My high school yearbook", "My company org chart" ];
potential_features = [ "Make it work on my phone", "Compare my IQ with friends", "Add my own private lists", "Add more lists", "Improve the clues and descriptions"];
values = [ "fun", "playable", "shareable", "useful", "engaging"];
named_questions = {
	welcome : {
		id : "welcome",
		q_type : "info_only",
		q_content : {
			header : "<h2>Welcome to MyCelebrityIQ!</h2><p>Test your knowledge of famous people and their accomplishments, in many different areas.</p><p>This is a very early test version of the site. Thanks for playing!</p>",
			submit_text : "Let's go!"
		}
	},

	when_score : {
		id : "when_score",
		q_type : "short_answer",
		q_content : {
			header : "<h2>So... when do I get my score?</h2><p>As soon as we collect enough answers! Please enter your email here, and we'll let you know the moment your score is ready.</p>",
			submit_text : "Done"
		}
	},

	faq1 : {
		id : "faq1",
		q_type : "info_only",
		q_content : {
			header : "<h2>FAQ #8: Is guessing okay?</h2><p>Yep. If you don't know, just take your best shot.</p>",
			submit_text : "Got it"
		}
	},

	faq2 : {
		id : "faq2",
		q_type : "info_only",
		q_content : {
			header : "<h2>How many questions do I need to answer to get my celebrity IQ?</h2><p>We don't know yet! That's something we're trying to learn right now. To help, please answer more questions, and invite your friends to play too!</p><p>PS: Our best guess is \"about 60.\"</p>",
			submit_text : "Got it"
		}
	},

	faq3 : {
		id : "faq3",
		q_type : "info_only",
		q_content : {
			header : "<h2>FAQ #23: Is it okay to look up the answers?</h2><p>Um, no. That's called cheating.</p><p>We have trained parrots who watch for signs of cheating, and squack loudly whenever they see anything suspicious.</p>",
			submit_text : "Okay"
		}
	},

	faq4 : {
		id : "faq4",
		q_type : "info_only",
		q_content : {
			header : "<h2>FAQ #34: How many celebrities does the game include?</h2><p>Pretty much all of them. We have over 40,000 people in our lists, with big plans to add more.</p>",
			submit_text : "Wow"
		}
	},

	faq5 : {
		id : "faq5",
		q_type : "info_only",
		q_content : {
			header : "<h2>FAQ #3: Why celebrities?</h2><p>We're not just interested in celebrities, we're interested in <i>people</i>.</p><p>An awful lot of our understanding of the world is reflected in the people we know and what we know about them. Celebrities are just the beginning&mdash;the people who happen to be known by a lot of other people.</p>",
			submit_text : "I see"
		}
	},

	email_signup : {
		id : "email_signup",
		q_type : "short_answer",
		q_content : {
			header : "<h2>Want to know your IQ?</h2><p>...</p>",
			submit_text : "Sign me up"
		}
	},

	new_list_mult_choice : {
		id : "new_list_mc_1",
		q_type : "mult_choice",
		q_content : {
			header : "<h2>Which new list of celebrities would you most like to see?</h2>",
			answers : _.map(_.range(0,5), function(i){return{id: i, val: potential_lists[i]}})
		}
	},

	new_list_mc_2 : {
		id : "new_list_mc_2",
		q_type : "mult_choice",
		q_content : {
			header : "<h2>Which new list of celebrities would you most like to see?</h2>",
			answers : _.map(_.range(5,10), function(i){return{id: i, val: potential_lists[i]}})
		}
	},

	new_list_mc_3 : {
		id : "new_list_mc_3",
		q_type : "mult_choice",
		q_content : {
			header : "<h2>Which new list of celebrities would you most like to see?</h2>",
			answers : _.map(_.range(10,15), function(i){return{id: i, val: potential_lists[i]}})
		}
	},

	new_list_mc_4 : {
		id : "new_list_mc_4",
		q_type : "mult_choice",
		q_content : {
			header : "<h2>Which new list of celebrities would you most like to see?</h2>",
			answers : _.map(_.range(15,20), function(i){return{id: i, val: potential_lists[i]}})
		}
	},

	new_list_oe : {
		id : "new_list_oe",
		q_type : "open_ended",
		q_content : {
			header : "<h2>We're always looking for new ideas for lists of celebrities to add. Any suggestions?</h2>",
			submit_text : 'Done'
		}
	},

	new_feature_oe : {
		id : "new_feature_oe",
		q_type : "open_ended",
		q_content : {
			header : "<h2>If you could make one improvement to this site, what would it be?</h2>",
			submit_text : 'Done'
		}
	},

	// new_feature_mc_1 : {
	// 	id : "new_feature_mc",
	// 	q_type : "mult_choice",
	// 	q_content : {
	// 		header : "<h2>If you could make one improvement to this site, what would it be?</h2>",
	// 		answers : _.map(_.range(0,5), function(i){return{id: i, val: potential_features[i]}})
	// 	}
	// },



// We're always looking for new ideas for lists of celebrities to add. Any suggestions?
// If you could make one improvement to this site, what would it be? [mult_choice and open_ended]
// How could we make this game more ...


};






// If you could add one list of celebrities, what would it be?

// We're always looking for new ideas for lists of celebrities to add. Any suggestions?
// Please name a celebrity who should definitely show up in this topic.


// Is it okay to look up the answers?
// Um, no. That's called cheating. We have trained parrots who watch for signs of cheating, and squack loudly whenever they see anything suspicious.

// Thanks

// Why PeopleIQ?
// If you know the people in an area, it's a good chang
