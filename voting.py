"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""
candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    """Register candidates with optional metadata.
    """
    if len(args) >= 1 and len(kwargs) == 0:
        for name in args:
            if name not in candidates:
                candidates.update({len(candidates) + 1: {"candidate_name": name}})
            else:
                print("Candidate already exists")

    elif len(args) == 1 and len(kwargs) >= 1:
        name = args[0]        
        if candidates:
            for can_id in candidates:
                if candidates[can_id]["candidate_name"] == name:
                    for key, value in kwargs.items():
                        candidates[can_id].update({key: value})
        else:
          print("User not found")

    else:
        return """
                Invalid passing of parameter
                Pass only candidate names to register multiple candidates at once
                Pass a single candidate name and the details you want to update
                """


def cast_vote(voter_id, candidate):
    """Cast vote if voter has not voted before.
        after all the vote logic is completeted sucessfully,
        return: Vote casted for {candidate}.
    """
    found_candidate = False
    if candidates:
        for can_id, can_details in candidates.items():
            if candidates[can_id]["candidate_name"] == candidate:
                found_candidate = True
                if voter_id not in voters:
                    voters.add(voter_id)
                    if "vote_count" in can_details:
                        candidates[can_id].update({"vote_count": candidates[can_id]["vote_count"] + 1}) 
                    else:                            candidates[can_id].update({"vote_count": 1})
                    return f"Vote casted for {candidate}"
                else:
                    return "Already voted"
        if not found_candidate:
            return f"Candidate {candidate} not found"
    else:
        return "No candidates yet"

def election_result():
    """Return the winner(s)."""
    # max_votes = #add logic
    # winners = #add logic
    # return {"winners": winners, "candidates": candidates}
    winners = []
    max_votes = 0
    for can_details in candidates.values():
        if "vote_count" in can_details:
            if can_details["vote_count"] > max_votes:
                max_votes = can_details["vote_count"]
   
    for can_id, can_details in candidates.items():
        if "vote_count" in can_details:
            if can_details["vote_count"] == max_votes:
                winners.append({can_id: can_details})

    return {"winners": winners, "candidates": candidates}

