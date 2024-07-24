SELECT 
    a.PLAYER_ID,
    a.PLAYER_NAME,
    a.scoring_average,
    b.SG_OTT,
    c.SG_APP,
    d.SG_ATG,
    e.SG_PUTTING, 
    f.sg_ttg,
    h.birdie_avg,
    i.driving_dist_yds,
    j.gir_pct
FROM 
    scoring_averages a
JOIN 
    sg_off_the_tee b ON a.PLAYER_ID = b.PLAYER_ID
JOIN
	sg_approach c ON a.PLAYER_ID = c.PLAYER_ID
JOIN 
    sg_around_the_green d ON a.PLAYER_ID = d.PLAYER_ID
JOIN 
    sg_putting e ON a.PLAYER_ID = e.PLAYER_ID
JOIN 
    sg_tee_to_green f ON a.PLAYER_ID = f.PLAYER_ID
JOIN 
    strokes_gained_total g ON a.PLAYER_ID = g.PLAYER_ID
JOIN 
    birdie_avg h ON a.PLAYER_ID = h.PLAYER_ID
JOIN
	driving_distance i ON a.PLAYER_ID = i.PLAYER_ID
JOIN
	gir_pct j ON a.PLAYER_ID = j.PLAYER_ID;