-- punto 1
SELECT u.idUsuario, u.nombreUsuario, t.fechaTweet, t.idTweet from usuario u INNER JOIN tweet t  ON u.idUsuario = t.uEmisor WHERE u.nombreUsuario LIKE 'c%' AND u.nombreUsuario NOT LIKE '%r' AND t.fechaTweet >= ADD_MONTHS(SYSDATE,-1);

-- punto 2
SELECT t.idTweet, t.fechaTweet, u.nombreUsuario, tw.idTweetRp, tw.fechaTweet FROM tweet t JOIN (SELECT idTweetRp, fechaTweet, COUNT(CASE WHEN idTweetRp IS NULL THEN 'FALSE' ELSE 'TRUE' END) FROM tweet GROUP BY idTweetRp, fechaTweet) tw ON tw.idTweetRp = t.idTweetRp INNER JOIN usuario u ON t.uEmisor = u.idUsuario WHERE u.nombreUsuario = 'eniland4w' ORDER BY t.fechaTweet DESC, tw.fechaTweet;

-- punto 3
SELECT u.idUsuario, u.nombreUsuario, s.sigueA FROM usuario u INNER JOIN seguidor s ON u.idUsuario = s.seguidor INNER JOIN usuario us ON us.idUsuario = s.sigueA WHERE us.nombreUsuario = 'chinchcliffel' AND us.nombreUsuario != 'pwoodroofe59';

-- punto 4
SELECT u.idUsuario, u.nombreUsuario, t.fechaTweet, tw.nombreUsuario FROM tweet t JOIN (SELECT s.idUsuario, s.nombreUsuario FROM usuario s WHERE s.nombreUsuario = 'cspurriar4h' OR s.nombreUsuario = 'arubinowitz3q') tw ON t.uEmisor = tw.idUsuario INNER JOIN destinatarioTweet d ON t.idTweet = d.idTweet LEFT JOIN usuario u ON u.idUsuario = d.uDestino WHERE t.fechaTweet >= ADD_MONTHS(SYSDATE,-12) ORDER BY t.fechaTweet DESC;

-- punto 5

-- punto 6
SELECT c.nombreCiudad, 
       rank() OVER (partition by c.nombreCiudad ORDER BY c.nombreCiudad DESC) Rank, 
    COUNT(c.codCiudad)
FROM ciudad c JOIN usuario u ON u.codCiudad = c.codCiudad INNER JOIN tweet t ON u.idUsuario = t.uEmisor GROUP BY c.nombreCiudad ORDER BY c.nombreCiudad;


-- punto 7
