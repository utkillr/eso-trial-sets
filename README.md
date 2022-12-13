# eso-trial-sets

This discord bot can tell which sets are good fit for certain bosses and which are not so good.  
It also give a little description of every trial, boss and set, which can come in handy for some memory refreshment

## Setup

You have to create a file `src/secret.json` with the following content:
```json
{
  "token": "<your bot token>"
}
```
This will configure the bot to work with provided token

## Launch

python bot.py

## Usage

Bot implements following commands:

### List trials
`/trials-list`  
Prints all the available trials with their description, and also prints name of each boss withing each trial

### Trial sets
`/trial-sets trial:<name> role:<role>`  
Prints description of trial and description of each boss. Description includes:
* Short summary on boss
* Sets to use
* Sets not to use

### Boss sets
`/boss-sets trial:<name> boss:<name> role:<role>`  
Prints description of boss and description of each set which should and should not be used on this boss.
Description of set included its mechanic and why should it be used or why should not it be used.
