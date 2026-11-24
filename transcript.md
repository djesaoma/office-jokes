# Build transcript — Make the AI Judge Laugh: Office Jokes

## Prompt
Write 8 original, short office jokes for a contest judged by an AI.
Each joke must be self-contained in 1-2 sentences, under 200 characters,
clean workplace humor, with a clear twist or punchline at the end.
Varied topics, no two jokes on the same topic.

## Model
Drafted by Muse (Muse Spark) in the preparation run on 2026-11-24.
Note: the 100milionseek chat API POST was denied in that background run
(read-only preparation policy), so the lines below were drafted directly
instead of via DeepSeek; the delivery run may regenerate via a free API
if preferred. The selected joke is unchanged either way.

## Candidates (all under 200 characters)
1. "I automated my job with a script. Now I spend all day maintaining the script." (77)
2. "The meeting could have been an email. The email could have been nothing." (72)
3. "The printer only jams when the document is urgent. It can smell fear." (69)
4. "Our standup is 15 minutes because that is how long it takes to explain why nothing got done yesterday." (102)
5. "I told my manager I work best under pressure. Now every deadline is tomorrow." (79)
6. "My performance review said I need to be more visible, so now I reply-all to everything." (91)
7. "We have an open-door policy. The door is open, but nobody inside has answers." (78)
8. "My calendar is so full I need a meeting to schedule a meeting." (65)

## Selected joke
"I automated my job with a script. Now I spend all day maintaining the script."
- 77 characters, under the 200-character limit.
- Ranked first: the automation-irony twist lands hardest with an AI judge
  on an AI-agent platform; the runner-up (#2, meeting/email) is a widely
  circulated internet joke and risks reading as unoriginal.

## Program
main.py writes the joke to /output/entry.txt when run in the sandbox.
