:- [wordnet/wn_s].
:- [wordnet/wn_g].
:- [wordnet/wn_hyp].
:- [wordnet/wn_ent].
:- [wordnet/wn_sim].
:- [wordnet/wn_mm].
:- [wordnet/wn_ms].
:- [wordnet/wn_mp].
:- [wordnet/wn_cs].
:- [wordnet/wn_vgp].
:- [wordnet/wn_at].
:- [wordnet/wn_ant].
:- [wordnet/wn_sa].
:- [wordnet/wn_ppl].
:- [wordnet/wn_per].
:- [wordnet/wn_fr].

paraphrase(S, R):-
    atomic_list_concat(P, ' ', S),
    paraphrase_do(P,O),
    atomic_list_concat(O, ' ', R).

go_deep(T, T).
go_deep(T, R):-
    paraphrase_do(T,R).

paraphrase_do([H|T],[H2|T2]):- 
    %print(sim1),
    s(Synset,_,H,Type,_,_), sim(Synset,Synset2), s(Synset2,_,H2,Type,_,_), H \= H2,
    go_deep(T, T2).

paraphrase_do([H1,H2|T],[H3|T2]):- 
    %print(sim2),
    atomic_list_concat([H1,H2], ' ', R),
    s(Synset,_,R,Type,_,_), sim(Synset,Synset2), s(Synset2,_,H3,Type,_,_),
    go_deep(T, T2).


%paraphrase_do([H|T],[H2|T2]):- 
%    %print(hyp1),
%    s(Synset,_,H,Type,_,_), hyp(Synset,Synset2), s(Synset2,_,H2,Type,_,_), H \= H2,
%    go_deep(T, T2).
%
%
%paraphrase_do([H1,H2|T],[H3|T2]):- 
%    %print(hyp2),
%    atomic_list_concat([H1,H2], ' ', R),
%    s(Synset,_,R,Type,_,_), hyp(Synset,Synset2), s(Synset2,_,H3,Type,_,_),
%    go_deep(T, T2).


paraphrase_do([H|T],[H2|T]):- 
    %print(ent1),
    s(Synset,_,H,Type,_,_), ent(Synset,Synset2), s(Synset2,_,H2,Type,_,_), H \= H2.

paraphrase_do([H1,H2|T],[H3|T]):- 
    %print(ent2),
    atomic_list_concat([H1,H2], ' ', R),
    s(Synset,_,R,Type,_,_), ent(Synset,Synset2), s(Synset2,_,H3,Type,_,_).

 paraphrase_do([H|T],[H2|T]):- 
     %print(vgp1),
     s(Synset,_,H,Type,_,_), vgp(Synset,_,Synset2,_), s(Synset2,_,H2,Type,_,_), H \= H2.

 paraphrase_do([H1,H2|T],[H3|T]):- 
     %print(vgp2),
     atomic_list_concat([H1,H2], ' ', R),
     s(Synset,_,R,Type,_,_), vgp(Synset,_,Synset2,_), s(Synset2,_,H3,Type,_,_).

paraphrase_do([H|T],[H2|T]):- 
    %print(sa1),
    s(Synset,_,H,Type,_,_), sa(Synset,_,Synset2,_), s(Synset2,_,H2,Type,_,_), H \= H2.

paraphrase_do([H1,H2|T],[H3|T]):- 
    %print(sa2),
    atomic_list_concat([H1,H2], ' ', R),
    s(Synset,_,R,Type,_,_), sa(Synset,_,Synset2,_), s(Synset2,_,H3,Type,_,_).

paraphrase_do([H1,H2|T],[H3|T]):- 
    %print(cs2),
    atomic_list_concat([H1,H2], ' ', R),
    s(Synset,_,R,Type,_,_), cs(Synset,Synset2), s(Synset2,_,H3,Type,_,_).

   
paraphrase_do([H|T],[H|R]):- 
    paraphrase_do(T,R).

example(1,R):- 
    print('She always speaks to him in a loud voice'),
    paraphrase('She always speaks to him in a loud voice',R).

example(2,R):- 
    print('Even intelligent people are sometimes absent-minded'),
    paraphrase('Even intelligent people are sometimes absent-minded',R).

example(3,R):- 
    print('They got there early, and they got really good seats'),
    paraphrase('They got there early, and they got really good seats',R).
