
-- Base de données :  `tennis`
--

-- --------------------------------------------------------

--
-- Structure de la table `tb_administration`
--

CREATE TABLE `tb_administration` (
  `id` int(11) NOT NULL,
  `id_membre` int(11) NOT NULL,
  `ajout_m` tinyint(1) NOT NULL DEFAULT 0,
  `changer_m` tinyint(1) NOT NULL DEFAULT 0,
  `import_membres` tinyint(1) NOT NULL DEFAULT 0,
  `ressources` varchar(20) NOT NULL DEFAULT '1'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Structure de la table `tb_courts`
--

CREATE TABLE `tb_courts` (
  `id_court` tinyint(4) NOT NULL,
  `nom` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `categorie` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `divers` text CHARACTER SET utf8 NOT NULL,
  `decalage` int(11) NOT NULL DEFAULT 0 COMMENT 'minutes',
  `duree` int(11) NOT NULL DEFAULT 60 COMMENT 'minutes',
  `horaires` text COLLATE utf8_unicode_ci NOT NULL,
  `etat` set('praticable','impraticable') COLLATE utf8_unicode_ci NOT NULL DEFAULT 'praticable',
  `date_etat` timestamp NOT NULL DEFAULT current_timestamp(),
  `visible` set('visible','invisible') COLLATE utf8_unicode_ci NOT NULL DEFAULT 'visible',
  `credit_invite` float NOT NULL DEFAULT 1,
  `credit_invite_jeune` float NOT NULL DEFAULT 1
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


--
-- Structure de la table `tb_equipes`
--

CREATE TABLE `tb_equipes` (
  `id` int(11) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `civilite` enum('H','F','JH','JF','H+35','H+45','H+55','H+65','F+35','F+45','F+55','F+65') NOT NULL,
  `annee` varchar(4) NOT NULL,
  `composition` varchar(40) NOT NULL,
  `infos` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `tb_equipes`
--

INSERT INTO `tb_equipes` (`id`, `nom`, `civilite`, `annee`, `composition`, `infos`) VALUES
(1, 'Seniors 1', 'H', '2013', '', ''),
(2, 'Equipe 1', 'H', '2013', '', '');

-- --------------------------------------------------------

--
-- Structure de la table `tb_log`
--

CREATE TABLE `tb_log` (
  `id` int(11) NOT NULL,
  `ip` varchar(20) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `action` varchar(80) NOT NULL,
  `infos` text NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `tb_membres`
--

CREATE TABLE `tb_membres` (
  `id_membre` int(11) UNSIGNED NOT NULL,
  `nom_p` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `login` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `date_naissance` date DEFAULT NULL,
  `sexe` set('M','F') COLLATE utf8_unicode_ci NOT NULL DEFAULT 'F',
  `courriel` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tel` varchar(34) COLLATE utf8_unicode_ci DEFAULT NULL,
  `categorie` set('-8','9/10','11/12','13/14','15/16','seniors','+35','+45','+55','+65') COLLATE utf8_unicode_ci NOT NULL,
  `validite` date NOT NULL DEFAULT '2007-10-15',
  `tickets` tinyint(4) NOT NULL DEFAULT 0,
  `ressources` varchar(30) COLLATE utf8_unicode_ci NOT NULL DEFAULT '1',
  `courriel_joomla` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `suspendu` date NOT NULL DEFAULT '0000-00-00',
  `notes` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci PACK_KEYS=1;

--

-- --------------------------------------------------------

--
-- Structure de la table `tb_membres_comp1`
--

CREATE TABLE `tb_membres_comp1` (
  `id` int(11) UNSIGNED NOT NULL,
  `licence` varchar(30) NOT NULL,
  `classement` enum('NC','40','30/5','30/4','30/3','30/2','30/1','30','15/5','15/4','15/3','15/2','15/1','15','5/6','4/6','3/6','2/6','1/6','0','-2/6','-4/6','-15','-30','Promotion') NOT NULL DEFAULT 'NC',
  `recherche` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Structure de la table `tb_passagers`
--

CREATE TABLE `tb_passagers` (
  `id` int(11) NOT NULL,
  `nom` varchar(40) NOT NULL,
  `courriel` varchar(50) NOT NULL,
  `id_reserv` int(11) NOT NULL,
  `ressource` int(11) NOT NULL,
  `regler` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- --------------------------------------------------------

--
-- Structure de la table `tb_prereservation`
--

CREATE TABLE `tb_prereservation` (
  `id_court` int(11) NOT NULL,
  `date_reserv` timestamp NULL DEFAULT '0000-00-00 00:00:00',
  `ressource` int(11) NOT NULL,
  `id_membre` int(11) NOT NULL,
  `fin` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `tb_recherches`
--

CREATE TABLE `tb_recherches` (
  `id` int(11) UNSIGNED NOT NULL,
  `etat` set('active','inactive') NOT NULL DEFAULT 'active',
  `id_membre` int(11) NOT NULL,
  `ressource` int(8) NOT NULL,
  `classement` text NOT NULL,
  `jour` set('lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche') NOT NULL,
  `periode` varchar(30) NOT NULL,
  `infos` text NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `id_alea` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `tb_reservations`
--

CREATE TABLE `tb_reservations` (
  `id_reserv` bigint(20) NOT NULL,
  `id_court` tinyint(4) NOT NULL,
  `id_personne` int(11) NOT NULL,
  `id_partenaire` int(11) DEFAULT NULL,
  `date_reserv` timestamp NULL DEFAULT NULL,
  `rens_club` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `renseignement` text COLLATE utf8_unicode_ci DEFAULT NULL,
  `id_alea` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `date_action` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `etat` enum('active','inactive') COLLATE utf8_unicode_ci NOT NULL DEFAULT 'active',
  `reservdouble` bigint(20) NOT NULL DEFAULT 0,
  `invite` int(11) NOT NULL DEFAULT 0 COMMENT '(tickets ou en euros)'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Structure de la table `tb_ressources`
--

CREATE TABLE `tb_ressources` (
  `id` int(5) NOT NULL,
  `tb_courts` varchar(30) NOT NULL,
  `tb_reservations` varchar(30) NOT NULL,
  `tb_membres` varchar(30) NOT NULL,
  `tb_membres_com` varchar(30) NOT NULL,
  `deb_horaire` float NOT NULL,
  `fin_horaire` float NOT NULL,
  `partenaires` int(1) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `Description` varchar(40) NOT NULL,
  `article` int(3) NOT NULL DEFAULT 1,
  `article_etendue` int(11) NOT NULL,
  `temps_double_reservation` int(10) NOT NULL DEFAULT 600,
  `intervalle_jours` float NOT NULL DEFAULT 7,
  `multi_reservation` tinyint(4) NOT NULL DEFAULT 0,
  `horaire_semaine_type` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



--
-- Structure de la table `xj36h_users`
--

CREATE TABLE `xj36h_users` (
  `id` int(11) NOT NULL,
  `name` varchar(400) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `password` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `block` tinyint(4) NOT NULL DEFAULT 0,
  `sendEmail` tinyint(4) DEFAULT 0,
  `registerDate` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `lastvisitDate` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `activation` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `params` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `lastResetTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'Date of last password reset',
  `resetCount` int(11) NOT NULL DEFAULT 0 COMMENT 'Count of password resets since lastResetTime',
  `otpKey` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT 'Two factor authentication encrypted keys',
  `otep` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT 'One time emergency passwords',
  `requireReset` tinyint(4) NOT NULL DEFAULT 0 COMMENT 'Require user to reset password on next login'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


--
-- Index pour les tables déchargées
--

--
-- Index pour la table `tb_administration`
--
ALTER TABLE `tb_administration`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_membre` (`id_membre`);

--
-- Index pour la table `tb_courriels`
--
ALTER TABLE `tb_courriels`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `tb_courts`
--
ALTER TABLE `tb_courts`
  ADD PRIMARY KEY (`id_court`);

--
-- Index pour la table `tb_entreprises`
--
ALTER TABLE `tb_entreprises`
  ADD UNIQUE KEY `id_2` (`id`),
  ADD KEY `id` (`id`),
  ADD KEY `id_3` (`id`);

--
-- Index pour la table `tb_equipes`
--
ALTER TABLE `tb_equipes`
  ADD KEY `id` (`id`);

--
-- Index pour la table `tb_log`
--
ALTER TABLE `tb_log`
  ADD UNIQUE KEY `id` (`id`);

--
-- Index pour la table `tb_mailing`
--
ALTER TABLE `tb_mailing`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `tb_membres`
--
ALTER TABLE `tb_membres`
  ADD PRIMARY KEY (`id_membre`),
  ADD UNIQUE KEY `login` (`login`),
  ADD KEY `validite` (`validite`);

--
-- Index pour la table `tb_membres_comp1`
--
ALTER TABLE `tb_membres_comp1`
  ADD KEY `id` (`id`);

--
-- Index pour la table `tb_paiements_membres`
--
ALTER TABLE `tb_paiements_membres`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `tb_paiements_type`
--
ALTER TABLE `tb_paiements_type`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `tb_parametres`
--
ALTER TABLE `tb_parametres`
  ADD PRIMARY KEY (`id_para`),
  ADD UNIQUE KEY `id_para` (`id_para`);

--
-- Index pour la table `tb_recherches`
--
ALTER TABLE `tb_recherches`
  ADD KEY `id` (`id`);

--
-- Index pour la table `tb_requetes`
--
ALTER TABLE `tb_requetes`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `tb_reservations`
--
ALTER TABLE `tb_reservations`
  ADD PRIMARY KEY (`id_reserv`),
  ADD KEY `date_reserv` (`date_reserv`),
  ADD KEY `etat` (`etat`),
  ADD KEY `id_court` (`id_court`),
  ADD KEY `id_personne` (`id_personne`),
  ADD KEY `id_partenaire` (`id_partenaire`);

--
-- Index pour la table `tb_ressources`
--
ALTER TABLE `tb_ressources`
  ADD UNIQUE KEY `id` (`id`);

--
-- Index pour la table `tb_stats_r1`
--
ALTER TABLE `tb_stats_r1`
  ADD UNIQUE KEY `jhi` (`jour`,`heure`,`id_court`);

--
-- Index pour la table `xj36h_users`
--
ALTER TABLE `xj36h_users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_name` (`name`(100)),
  ADD KEY `idx_block` (`block`),
  ADD KEY `username` (`username`),
  ADD KEY `email` (`email`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `tb_administration`
--
ALTER TABLE `tb_administration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT pour la table `tb_courriels`
--
ALTER TABLE `tb_courriels`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `tb_courts`
--
ALTER TABLE `tb_courts`
  MODIFY `id_court` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT pour la table `tb_entreprises`
--
ALTER TABLE `tb_entreprises`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `tb_equipes`
--
ALTER TABLE `tb_equipes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `tb_log`
--
ALTER TABLE `tb_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `tb_mailing`
--
ALTER TABLE `tb_mailing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `tb_membres`
--
ALTER TABLE `tb_membres`
  MODIFY `id_membre` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT pour la table `tb_paiements_membres`
--
ALTER TABLE `tb_paiements_membres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `tb_paiements_type`
--
ALTER TABLE `tb_paiements_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT pour la table `tb_parametres`
--
ALTER TABLE `tb_parametres`
  MODIFY `id_para` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT pour la table `tb_recherches`
--
ALTER TABLE `tb_recherches`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `tb_requetes`
--
ALTER TABLE `tb_requetes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `tb_reservations`
--
ALTER TABLE `tb_reservations`
  MODIFY `id_reserv` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87672;

--
-- AUTO_INCREMENT pour la table `xj36h_users`
--
ALTER TABLE `xj36h_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=978;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
