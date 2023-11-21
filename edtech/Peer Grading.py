def peer_grading(peer_answers, student_answer):
    
    peer_feedback = {}
    for peer, answer in peer_answers.items():
        
        similarity_score = calculate_similarity(answer, student_answer)
        peer_feedback[peer] = similarity_score
    return peer_feedback
