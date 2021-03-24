def bowling_game(scorecard):

    # The separator in the input string is the "-" character
    score_split_frames = scorecard.split("-")

    # Gets length of tenth frame (last index in list)
    tenth_frame_length = len(score_split_frames[-1])

    # Creates a list, scorecard, by joining the iterable score_split_frames with empty string
    scorecard = list("".join(score_split_frames))

    final_score = 0

    # Calculates final score by going through the scorecard, starts at special tenth frame
    for entry in range(len(scorecard) - 1, -1, -1):

        # X string is a strike

        if scorecard[entry] == "X":

            scorecard[entry] = 10

            # Check if tenth frame

            if entry < len(scorecard) - tenth_frame_length:

                # If strike, add next two bowls to score

                final_score += int(scorecard[entry + 1]) + int(scorecard[entry + 2])

        # # / string is a spare

        elif scorecard[entry] == "/":

            # Whatever the score was in first bowl of frame, [10 - (first bowl)] will be second bowl score for a spare

            scorecard[entry] = 10 - int(scorecard[entry - 1])

            # Check if tenth frame

            if entry < len(scorecard) - 1:

                final_score += int(scorecard[entry + 1])

        # Current score entry is added on to final score

        final_score += int(scorecard[entry])

    return final_score


# Testing the three example scorecards
test_scorecards = ["X-X-X-X-X-X-X-X-X-XXX", "45-54-36-27-09-63-81-18-90-72", "5/-5/-5/-5/-5/-5/-5/-5/-5/-5/-5"]

for currScorecard in test_scorecards:

    print("Scorecard: " + currScorecard)

    print("Final Score: " + str(bowling_game(currScorecard)))
