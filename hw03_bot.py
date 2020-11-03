import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment functions from the week_07 lab here
def generate_comment_0():
    biden_names = ['Joe Biden', 'Biden', 'Joe', 'Mr. Biden', 'Joseph Robinette Biden Jr.']
    biden_name = random.choice(biden_names)
    good_feeelings = ['like', 'support', 'endorse', 'am a fan of', 'will vote for']
    good_feeling = random.choice(good_feeelings)
    roles = ['president', 'US Master', 'king', 'superior human of the nation', 'nation savior']
    role = random.choice(roles)
    adjectives = ['funny', 'great', 'cool', 'interesting', 'awesome']
    adjective = random.choice(adjectives)
    traits = ['smile', 'personality', 'plan', 'handshake', 'laugh']
    trait = random.choice(traits)
    text = 'I ' + good_feeling + ' ' + biden_name + ' as ' + role + ' because he has a ' + adjective + ' ' + trait + '. ' + biden_name + ' is also ' + trait + '.'
    return text

def generate_comment_1():
    biden_names = ['Joe Biden', 'Biden', 'Joe', 'Mr. Biden', 'Joseph Robinette Biden Jr.']
    biden_name = random.choice(biden_names)
    verbs = ['ready', 'prepared', 'eager', 'motivated', 'inspired']
    verb = random.choice(verbs)
    actions = ['remake America.', 'solve everything.', 'be master of the US.', 'dethrone Trump.', 'win.']
    action = random.choice(actions)
    rankings = ['greatest', 'awesomest', 'best', 'coolest', 'funniest']
    ranking = random.choice(rankings)
    americas = ['the US', 'America', 'USA', "'murica", 'the nation']
    america = random.choice(americas)
    text1 = biden_name + ' is ' + verb + ' to ' + action + ' He will be the ' + ranking + ' president of ' + america + '.'
    return text1

def generate_comment_2():
    biden_names = ['Joe Biden', 'Biden', 'Joe', 'Mr. Biden', 'Joseph Robinette Biden Jr.']
    biden_name = random.choice(biden_names)
    roles = ['president', 'US Master', 'king', 'superior human of the nation', 'nation savior']
    role = random.choice(roles)
    americas = ['the US', 'America', 'USA', "'murica", 'the nation']
    america = random.choice(americas)
    results = ['great', 'awesome', 'supreme', 'extraordinary', 'incredible']
    result = random.choice(results)
    adjs = ['cool', 'smart', 'caring', 'determined', 'loyal']
    adj = random.choice(adjs)
    text2 = 'If ' + biden_name + ' is elected ' + role + ', he will make ' + america + ' ' + result + '. He is so ' + adj + '.'
    return text2

def generate_comment_3():
    trump_names = ['Donald Trump', 'Trump', 'DT', 'The Don', 'Mr. President']
    trump_name = random.choice(trump_names)
    roles = ['president', 'US Master', 'king', 'superior human of the nation', 'nation savior']
    role = random.choice(roles)
    destroys = ['destoy', 'damage', 'exterminate', 'ruin', 'wreck']
    destroy = random.choice(destroys)
    nations = ['country', 'nation', 'home', 'homeland', 'empire']
    nation = random.choice(nations)
    bad_trumps = ['crazy man', 'whacko', 'mad man', 'weirdo']
    bad_trump = random.choice(bad_trumps)
    text3 = 'If ' + trump_name + ' is reelected as ' + role + ', he will ' + destroy + ' our ' + nation + '. Do not let this ' + bad_trump + ' do that.'
    return text3

def generate_comment_4():
    trump_names = ['Donald Trump', 'Trump', 'DT', 'The Don', 'Mr. President']
    trump_name = random.choice(trump_names)
    trump_adjs = ['mean', 'dumb', 'crazy', 'distracted', 'unkind']
    trump_adj = random.choice(trump_adjs)
    biden_names = ['Joe Biden', 'Biden', 'Joe', 'Mr. Biden', 'Joseph Robinette Biden Jr.']
    biden_name = random.choice(biden_names)
    rates = ['cooler', 'smarter', 'nicer', 'kinder', 'sharper']
    rate = random.choice(rates)
    good_feeelings = ['like', 'support', 'endorse', 'am a fan of', 'will vote for']
    good_feeling = random.choice(good_feeelings)
    text4 = 'Do not vote for ' + trump_name + ', he is so ' + trump_adj + '.' + biden_name + ' is way ' + rate + ' which is why I ' + good_feeling + ' him.'
    return text4

def generate_comment_5():
    trump_names = ['Donald Trump', 'Trump', 'DT', 'The Don', 'Mr. President']
    trump_name = random.choice(trump_names)
    roles = ['president', 'US Master', 'king', 'superior human of the nation', 'nation savior']
    role = random.choice(roles)
    americas = ['the US', 'America', 'USA', "'murica", 'the nation']
    america = random.choice(americas)
    destroys = ['destoy', 'damage', 'exterminate', 'ruin', 'wreck']
    destroy = random.choice(destroys)
    elections = ['win. ', 'be elected.', 'be crowned king.', 'triumph.']
    election = random.choice(elections)
    text5 = trump_name + ' cannot be ' + role + ' again. He will take ' + america + ' and ' + destroy + ' it. He cannot ' + election
    return text5

for i in range (10):
    def generate_comment():
        options = [0,1,2,3,4,5]
        choice = random.choice(options)
        if choice == 0:
            return generate_comment_0()
        elif choice == 1:
            return generate_comment_1()
        elif choice == 2:
            return generate_comment_2()
        elif choice == 3:
            return generate_comment_3()
        elif choice == 4: 
            return generate_comment_4()
        elif choice == 5:
            return generate_comment_5()

# connect to reddit 
reddit = praw.Reddit('bot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jm338w/another_debate_post/?sort=new'
submission = reddit.submission(url=reddit_debate_url)
submission.comments.replace_more(limit = None)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
start_time = datetime.datetime.now()

# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    all_comments = submission.comments.list()
    print('len(all_comments)=',len(all_comments))
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    my_comments = []
    for comment in all_comments:
        if comment.author == 'valeriasbot':
            my_comments.append(comment)
        else:
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))
    print('len(my_comments)=',len(my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments)
    
        # FIXME (task 2)
         # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

    if has_not_commented == len(all_comments):
        try:
            submission.reply(generate_comment())
        except: 
            print('exception found')
            print('starting to sleep')
            time.sleep(60)
            print('done sleeping')

        print(generate_comment())


        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
    else:
                comments_without_replies = []
                for comment in not_my_comments:
                    replied = True
                    for comment.reply in not_my_comments: 
                        if comment.author == 'valeriasbot':
                            replied = True
                            break 
                        if comment.author != 'valeriasbot':
                            replied = False 
                    if replied:
                        continue
                    else:
                        comments_without_replies.append(comment) 
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
    print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
    try:
            try:
                comment = reddit.comment(id=random.choice(comments_without_replies))
                print('comment_id =', random.choice(comments_without_replies))
                comment.reply(generate_comment())
            except:
                pass
    except: #AssertionError
            print('exception found')
            print('starting to sleep')
            time.sleep(60)
            print('done sleeping')
                
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
    result = random.random()
    all_submissions = []
    if result >= 0.5:
        print('original submission')
        submission = reddit.submission(url='https://www.reddit.com/r/csci040temp/comments/jj7fo1/hello_debate_test_hello/')
        submission.reply(generate_comment())
    if result < 0.5:
        print('top subreddit submission')
        # print(type(all_submissions))
        # for submission in reddit.subreddit("csci040").top("month"):
        for submission in reddit.subreddit("csci040temp").top("day"):
            # print(submission.title)
            all_submissions.append(submission)
            # print(submission.title)
        # print(len(all_submissions))
        submission_choice = random.choice(all_submissions)
        submission = reddit.submission(id=submission_choice)
        print('submission_id =',submission_choice)
        print(submission_choice.title)
        # print(type(submission_choice))        
        # submission.reply(generate_comment())
        # print(generate_comment())


# extra creditz 
# task 6 - upvoting a comment
biden = ['Biden', "Joe", 'Joseph Robinette Biden Jr', 'Mr. Biden']
for comment in submission.comments.list():
    if biden in comment.body.lower():
        comment.upvote()

# task 7 - downvoting a comment 
trump = ['Trump', 'Donald Trump', 'The Don']
for comment in submission.comments.list():
    if trump in comment.body.lower():
        comment.downvote() 

# task 8 - upvoting submission 
for submission in reddit.subreddit('csci040temp'):
    if biden in submission: 
        submission.upvote()

# task 9 - downvoting submission 
for submission in reddit.subreddit('csci040temp'):
    if trump in submission: 
        submission.downvote()