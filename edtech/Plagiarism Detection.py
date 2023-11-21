from difflib import SequenceMatcher

def plagiarism_detection(answer1, answer2):
    
    similarity_ratio = SequenceMatcher(None, answer1, answer2).ratio()
    if similarity_ratio > 0.8:
        return "Potential plagiarism detected"
    else:
        return "No significant similarity found"
