<?php
/**
*
* acp_styles.php [Slovak]
*
* @package language
* @version $Id: styles.php,v 1.39 2007/07/16 23:06:42 naderman Exp $
* @copyright (c) 2005 phpBB Group
* @license http://opensource.org/licenses/gpl-license.php GNU Public License
*
*/

/**
* DO NOT CHANGE
*/
if (!defined('IN_PHPBB'))
{
	exit;
}

if (empty($lang) || !is_array($lang))
{
	$lang = array();
}

// DEVELOPERS PLEASE NOTE
//
// All language files should use UTF-8 as their encoding and the files must not contain a BOM.
//
// Placeholders can now contain order information, e.g. instead of
// 'Page %s of %s' you can (and should) write 'Page %1$s of %2$s', this allows
// translators to re-order the output of data while ensuring it remains correct
//
// You do not need this where single placeholders are used, e.g. 'Message %d' is fine
// equally where a string contains only two placeholders which are used to wrap text
// in a url you again do not need to specify an order e.g., 'Click %sHERE%s' is fine

$lang = array_merge($lang, array(
	'ACP_IMAGESETS_EXPLAIN'	=> 'Sada obrázkov obsahuje všetky obrázky pre tlačidlá fóra, priečinky a veľa ďalších vecí na celom fóre. Tu môžete upraviť, exportovať alebo odstrániť existujúcu sadu obrázkov alebo pridať a importovať nové sady.',
	'ACP_STYLES_EXPLAIN'	=> 'Tu môžete upravovať dostupné štýly pre vaše fórum. Štýl sa skladá zo šablóny, témy a sady obrázkov. Môžete upravovať existujúce štýly, odstraňovať ich, deaktivovať, reaktivovať, vytvárať nové, importovať a oveľa viac. Môžete sa pozrieť ako daný štýl vypadá použitím ukážky. Zvolený predvolený štýl je označený hviezdičkou (*). Je tu tiež uvedené, koľko používateľov používa tento štýl.',
	'ACP_TEMPLATES_EXPLAIN'	=> 'Šablóna zahŕňa celý kód, ktorý tvorí vzhľad stránky. Tu môžete upraviť existujúce šablóny, exportovať ich, importovať nové alebo sa pozrieť, ako daný štýl vyzerá použitím funkcie ukážky. Môžete tiež upraviť šablónu, ktorá generuje značky BBCode.',
	'ACP_THEMES_EXPLAIN'	=> 'Tu môžete vytvárať, inštalovať, upravovať, odstraňovať alebo exportovať témy. Téma je kombinácia farieb a obrázkov, ktoré sú aplikované na šablóny na vytvorenie finálneho vzhľadu vášho fóra. Možnosti nastavení sú závislé na konfigurácií vášho servera a phpBB, ak chcete vedieť viac, pozrite si manuál. Pri vytváraní novej témy tiež môžete použiť už existujúcu ako základ.',
	'ADD_IMAGESET'			=> 'Vytvoriť sadu obrázkov',
	'ADD_IMAGESET_EXPLAIN'	=> 'Tu môžete vytvoriť novú sadu obrázkov. Podľa nastavení servera a oprávnení k súborom vám tu budú ponúknuté rôzne možnosti nastavení. Napr. budete môcť založiť novú sadu obrázkov na už existujúcej. Budete tiež môcť odoslať alebo importovať (z ukladacieho priečinka) archív so sadou obrázkov. Pokiaľ budete importovať sadu obrázkov z archívu, názov môže byť zvolený podľa názvu daného archívu, pokiaľ tak chcete spraviť, nechajte pole názvu sady prázdne.',
	'ADD_STYLE'				=> 'Vytvoriť štýl',
	'ADD_STYLE_EXPLAIN'		=> 'Tu môžete vytvoriť nový štýl. Podľa nastavení servera a oprávnení k súborom vám tu budú ponúknuté rôzne možnosti nastavení. Napr. budete môcť založiť nový štýl na už existujúcom. Budete tiež môcť odoslať alebo importovať (z ukladacieho priečinka) archív so štýlom. Pokiaľ odosielate alebo importujete štýl, názov bude zistený automaticky.',
	'ADD_TEMPLATE'			=> 'Vytvoriť šablónu',
	'ADD_TEMPLATE_EXPLAIN'	=> 'Tu môžete pridať novú šablónu. Podľa nastavení servera a oprávnení k súborom vám tu budú ponúknuté rôzne možnosti nastavení. Napr. budete môcť založiť novú sadu šablón na už existujúcej. Budete tiež môcť odoslať alebo importovať (z ukladacieho priečinka) archív so šablónou. Pokiaľ budete importovať šablónu z archívu, názov môže byť zvolený podľa názvu daného archívu, pokiaľ tak chcete spraviť, nechajte pole názvu šablóny prázdne.',
	'ADD_THEME'				=> 'Vytvoriť tému',
	'ADD_THEME_EXPLAIN'		=> 'Tu môžete pridať novú tému. Podľa nastavení servera a oprávnení k súborom vám tu budú ponúknuté rôzne možnosti nastavení. Napr. budete môcť založiť novú tému na už existujúcej. Budete tiež môcť odoslať alebo importovať (z ukladacieho priečinka) archív s témou. Pokiaľ budete importovať tému z archívu, názov môže byť zvolený podľa názvu daného archívu, pokiaľ tak chcete spraviť, nechajte pole názvu témy prázdne.',
	'ARCHIVE_FORMAT'		=> 'Typ archívu',
	'AUTOMATIC_EXPLAIN'		=> 'Nechajte prázdne pre automatickú detekciu.',

	'BACKGROUND'			=> 'Pozadie',
	'BACKGROUND_COLOUR'		=> 'Farba pozadia',
	'BACKGROUND_IMAGE'		=> 'Obrázok na pozadí',
	'BACKGROUND_REPEAT'		=> 'Opakovanie pozadia',
	'BOLD'					=> 'Tučné',

	'CACHE'							=> 'Vyrovnávacia pamäť',
	'CACHE_CACHED'					=> 'Vo vyrovnávacej pamäti',
	'CACHE_FILENAME'				=> 'Súbor šablóny',
	'CACHE_FILESIZE'				=> 'Veľkosť súboru',
	'CACHE_MODIFIED'				=> 'Upravené',
	'CONFIRM_IMAGESET_REFRESH'		=> 'Naozaj chcete obnoviť všetky údaje sady obrázkov? Nastavenie z konfiguračného súboru sady obrázkov prepíšu všetky úpravy, ktoré boli vykonané cez zabudovaný editor a sú uložené v databáze.',
	'CONFIRM_TEMPLATE_CLEAR_CACHE'	=> 'Naozaj chcete odstrániť všetky verzie súborov šablón nachádzajúce sa vo vyrovnávacej pamäti?',
	'CONFIRM_TEMPLATE_REFRESH'		=> 'Naozaj chcete obnoviť všetky údaje šablón uložených v databáze nahraním hodnôt zo súborov uložených v súborov systéme servera? Toto prepíše všetky úpravy, ktoré boli vykonané cez zabudovaný editor a sú uložené v databáze.',
	'CONFIRM_THEME_REFRESH'			=> 'Naozaj chcete obnoviť všetky údaje tém uložených v databáze nahraním hodnôt zo súborov uložených v súborov systéme servera? Toto prepíše všetky úpravy, ktoré boli vykonané cez zabudovaný editor a sú uložené v databáze.',
	'COPYRIGHT'						=> 'Copyright',
	'CREATE_IMAGESET'				=> 'Vytvoriť novú sadu obrázkov',
	'CREATE_STYLE'					=> 'Vytvoriť nový štýl',
	'CREATE_TEMPLATE'				=> 'Vytvoriť novú šablónu',
	'CREATE_THEME'					=> 'Vytvoriť novú tému',
	'CURRENT_IMAGE'					=> 'Aktuálny obrázok',

	'DEACTIVATE_DEFAULT'		=> 'Nemôžete deaktivovať predvolený štýl.',
	'DELETE_FROM_FS'			=> 'Odstrániť zo súborového systému',
	'DELETE_IMAGESET'			=> 'Odstrániť sadu obrázkov',
	'DELETE_IMAGESET_EXPLAIN'	=> 'Tu môžete odstrániť vybranú sadu obrázkov z databázy. Pokiaľ máte dostatočné oprávnenia, môžete ju odstrániť aj zo súborového systému. Pamätajte, že toto sa nedá vrátiť. Akonáhle je sada odstránená, nedá sa obnoviť. Odporúčame najskôr urobiť export do archívu pre neskoršie použitie.',
	'DELETE_STYLE'				=> 'Odstrániť štýl',
	'DELETE_STYLE_EXPLAIN'		=> 'Tu môžete odstrániť vybraný štýl. Tu sa ale nedajú odstrániť jeho súčasti, tie musíte odstrániť každú zvlášť v odpovedajúcich sekciách. Odstránenie štýlu je trvalé a nedá sa vrátiť späť.',
	'DELETE_TEMPLATE'			=> 'Odstrániť šablónu',
	'DELETE_TEMPLATE_EXPLAIN'	=> 'Tu môžete odstrániť vybranú sadu šablón z databázy. Pokiaľ máte dostatočné oprávnenia, môžete ju odstrániť aj zo súborového systému. Pamätajte, že toto sa nedá vrátiť. Akonáhle je sada odstránená, nedá sa obnoviť. Odporúčame najskôr urobiť export do archívu pre neskoršie použitie.',
	'DELETE_THEME'				=> 'Odstrániť tému',
	'DELETE_THEME_EXPLAIN'		=> 'Tu môžete odstrániť vybranú tému z databázy. Pokiaľ máte dostatočné oprávnenia, môžete ju odstrániť aj zo súborového systému. Pamätajte, že toto sa nedá vrátiť. Akonáhle je sada odstránená, nedá sa obnoviť. Odporúčame najskôr urobiť export do archívu pre neskoršie použitie.',
	'DETAILS'					=> 'Detaily',
	'DIMENSIONS_EXPLAIN'		=> 'Zvolením budú pridané informácie o rozmeroch obrázka',

	'EDIT_DETAILS_IMAGESET'				=> 'Upraviť detaily sady obrázkov',
	'EDIT_DETAILS_IMAGESET_EXPLAIN'		=> 'Tu môžete upravovať niektoré detaily sady obrázkov, napr. ich názov.',
	'EDIT_DETAILS_STYLE'				=> 'Upraviť štýl',
	'EDIT_DETAILS_STYLE_EXPLAIN'		=> 'Týmto formulárom môžete upraviť existujúci štýl. Môžete tiež zvoliť kombinácie šablón, sady obrázkov a skinov, ktoré tento štýl tvoria. Môžete tiež označiť tento štýl ako predvolený.',
	'EDIT_DETAILS_TEMPLATE'				=> 'Upraviť detaily šablóny',
	'EDIT_DETAILS_TEMPLATE_EXPLAIN'		=> 'Tu môžete upraviť niektoré nastavenia šablóny, napr. jej názov. Môžete tiež zvoliť, či použiť štýl z .css súboru alebo štýly z databázy. Táto možnosť závisí na nastaveniach PHP a či do vašej šablóny môže zapisovať webový server.',
	'EDIT_DETAILS_THEME'				=> 'Upraviť detaily témy',
	'EDIT_DETAILS_THEME_EXPLAIN'		=> 'Tu môžete upraviť niektoré nastavenia témy, napr. jej názov. Môžete tiež zvoliť, či použiť štýl z .css súboru alebo štýly z databázy. Táto možnosť závisí na nastaveniach PHP a či do vašej témy môže zapisovať webový server.',
	'EDIT_IMAGESET'						=> 'Upraviť sadu obrázkov',
	'EDIT_IMAGESET_EXPLAIN'				=> 'Tu môžete upraviť jednotlivé obrázky, ktoré tvoria celú sadu. Môžete tiež nastaviť rozmery týchto obrázkov. Rozmery sú voliteľné, ale môžu predísť niektorým problémom s vykresľovaním v niektorých prehliadačoch. Môžete ušetriť trochu miesta v databáze, pokiaľ ich neuvediete.',
	'EDIT_TEMPLATE'						=> 'Upraviť šablónu',
	'EDIT_TEMPLATE_EXPLAIN'				=> 'Tu môžete priamo upraviť šablónu. Majte na pamäti, že tieto zmeny sú trvalé a nedajú vrátiť späť. Pokiaľ má PHP príslušné oprávnenia, priamo upraví súbory šablóny. Pokiaľ ich nemá, zmeny budú uložené v databáze a nahrávané odtiaľ. Buďte opatrný pri úprave vašej šablóny, nezabudnite uzavrieť všetky premenné {XXXX} a podmienené výrazy.',
	'EDIT_TEMPLATE_STORED_DB'			=> 'Súbor šablóny nie je zapisovateľný, takže úpravy boli uložené v databáze.',
	'EDIT_THEME'						=> 'Upraviť tému',
	'EDIT_THEME_EXPLAIN'				=> 'Tu môžete upraviť vybranú tému, meniť farby, obrázky atď.',
	'EDIT_THEME_STORED_DB'				=> 'Súbor štýlov nie je zapisovateľný, takže úpravy boli uložené v databáze.',
	'EDIT_THEME_STORE_PARSED'			=> 'Téma vyžaduje spracovaný štýl. Toto je možné len prípade, že je uložená v databáze.',
	'EXPORT'							=> 'Exportovať',

	'FOREGROUND'			=> 'Popredie',
	'FONT_COLOUR'			=> 'Farba písma',
	'FONT_FACE'				=> 'Štýl písma',
	'FONT_FACE_EXPLAIN'		=> 'Môžete zvoliť viac typov písma použitím čiarok. Pokiaľ používateľ nemá nainštalovaný prvé písmo, bude použité nasledujúce.',
	'FONT_SIZE'				=> 'Veľkosť písma',

	'GLOBAL_IMAGES'			=> 'Globálne',

	'HIDE_CSS'				=> 'Skryť čisté CSS',

	'IMAGE_WIDTH'				=> 'Šírka obrázka',
	'IMAGE_HEIGHT'				=> 'Výška obrázka',
	'IMAGE'						=> 'Obrázok',
	'IMAGE_NAME'				=> 'Názov obrázka',
	'IMAGE_PARAMETER'			=> 'Parameter',
	'IMAGE_VALUE'				=> 'Hodnota',
	'IMAGESET_ADDED'			=> 'Nová sada obrázkov nahraná do súborového systému.',
	'IMAGESET_ADDED_DB'			=> 'Nová sada obrázkov pridaná do databázy.',
	'IMAGESET_DELETED'			=> 'Sada obrázkov bola úspešne odstránená',
	'IMAGESET_DELETED_FS'		=> 'Sada obrázkov bola odstránená z databáze, ale niektoré súbory mohli zostať v súborovom systéme.',
	'IMAGESET_DETAILS_UPDATED'	=> 'Nastavenie sady obrázkov bolo úspešne aktualizované',
	'IMAGESET_ERR_ARCHIVE'		=> 'Prosím, zvoľte archivačnú metódu',
	'IMAGESET_ERR_COPY_LONG'	=> 'Copyright nemôže byť dlhší ako 60 znakov.',
	'IMAGESET_ERR_NAME_CHARS'	=> 'Názov sady obrázkov môže obsahovať len alfanumerické znaky, -, +, _ a medzeru.',
	'IMAGESET_ERR_NAME_EXIST'	=> 'Sada obrázkov s týmto označením už existuje.',
	'IMAGESET_ERR_NAME_LONG'	=> 'Názov sady obrázkov nesmie byť dlhší ako 30 znakov.',
	'IMAGESET_ERR_NOT_IMAGESET'	=> 'Zvolený archív neobsahuje platnú sadu obrázkov.',
	'IMAGESET_ERR_STYLE_NAME'	=> 'Musíte zvoliť názov sady obrázkov.',
	'IMAGESET_EXPORT'			=> 'Exportovať sadu',
	'IMAGESET_EXPORT_EXPLAIN'	=> 'Tu môžete exportovať zvolenú sadu obrázkov v archíve. Archív bude obsahovať všetky potrebné údaje na prenesenie na iné fórum. Môžete si vybrať medzi uložením archívu do ukladacieho priečinka, jeho stiahnutím alebo nahraním cez FTP.',
	'IMAGESET_EXPORTED'			=> 'Sada obrázkov bola úspešne exportovaná a uložená v %s.',
	'IMAGESET_NAME'				=> 'Názov sady obrázkov',
	'IMAGESET_REFRESHED'		=> 'Sada bola úspešne obnovená.',
	'IMAGESET_UPDATED'			=> 'Sada bola úspešne aktualizovaná.',
	'ITALIC'					=> 'Kurzíva',

	'IMG_CAT_BUTTONS'		=> 'Preložené tlačidlá',
	'IMG_CAT_CUSTOM'		=> 'Vlastné obrázky',
	'IMG_CAT_FOLDERS'		=> 'Ikony tém',
	'IMG_CAT_FORUMS'		=> 'Ikony fór',
	'IMG_CAT_ICONS'			=> 'Všeobecné ikony',
	'IMG_CAT_LOGOS'			=> 'Logá',
	'IMG_CAT_POLLS'			=> 'Obrázky hlasovaní',
	'IMG_CAT_UI'			=> 'Všeobecné prvky používateľského rozhrania',
	'IMG_CAT_USER'			=> 'Ďalšie obrázky',

	'IMG_SITE_LOGO'			=> 'Hlavné logo',
	'IMG_UPLOAD_BAR'		=> 'Ukazovateľ priebehu odosielania',
	'IMG_POLL_LEFT'			=> 'Ľavý okraj hlasovania',
	'IMG_POLL_CENTER'		=> 'Stred hlasovania',
	'IMG_POLL_RIGHT'		=> 'Pravý okraj hlasovania',
	'IMG_ICON_FRIEND'		=> 'Pridať priateľa',
	'IMG_ICON_FOE'			=> 'Pridať nepriateľa',

	'IMG_FORUM_LINK'			=> 'Fórum ako odkaz',
	'IMG_FORUM_READ'			=> 'Fórum',
	'IMG_FORUM_READ_LOCKED'		=> 'Zamknuté fórum',
	'IMG_FORUM_READ_SUBFORUM'	=> 'Subfórum',
	'IMG_FORUM_UNREAD'			=> 'Neprečítané príspevky vo fóre',
	'IMG_FORUM_UNREAD_LOCKED'	=> 'Neprečítané príspevky vo fóre - zamknuté',
	'IMG_FORUM_UNREAD_SUBFORUM'	=> 'Neprečítané príspevky v subfóre',
	'IMG_SUBFORUM_READ'			=> 'Ikona subfóra',
	'IMG_SUBFORUM_UNREAD'		=> 'Ikona subfóra s neprečítanými príspevkami',

	'IMG_TOPIC_MOVED'			=> 'Presunutá téma',

	'IMG_TOPIC_READ'				=> 'Téma',
	'IMG_TOPIC_READ_MINE'			=> 'Téma, do ktorej som prispel',
	'IMG_TOPIC_READ_HOT'			=> 'Obľúbená téma',
	'IMG_TOPIC_READ_HOT_MINE'		=> 'Obľúbená téma, do ktorej som prispel',
	'IMG_TOPIC_READ_LOCKED'			=> 'Zamknutá téma',
	'IMG_TOPIC_READ_LOCKED_MINE'	=> 'Zamknutá téma, do ktorej som prispel',

	'IMG_TOPIC_UNREAD'				=> 'Téma s neprečítanými príspevkami',
	'IMG_TOPIC_UNREAD_MINE'			=> 'Téma s neprečítanými príspevkami, do ktorej som prispel',
	'IMG_TOPIC_UNREAD_HOT'			=> 'Obľúbená téma s neprečítanými príspevkami',
	'IMG_TOPIC_UNREAD_HOT_MINE'		=> 'Obľúbená téma s neprečítanými príspevkami, do ktorej som prispel',
	'IMG_TOPIC_UNREAD_LOCKED'		=> 'Zamknutá téma s neprečítanými príspevkami',
	'IMG_TOPIC_UNREAD_LOCKED_MINE'	=> 'Zamknutá téma s neprečítanými príspevkami, do ktorej som prispel',

	'IMG_STICKY_READ'				=> 'Oznámenie',
	'IMG_STICKY_READ_MINE'			=> 'Oznámenie, do ktorého som prispel',
	'IMG_STICKY_READ_LOCKED'		=> 'Zamknuté oznámenie',
	'IMG_STICKY_READ_LOCKED_MINE'	=> 'Zamknuté oznámenie, do ktorého som prispel',
	'IMG_STICKY_UNREAD'				=> 'Oznámenie s neprečítanými príspevkami',
	'IMG_STICKY_UNREAD_MINE'		=> 'Oznámenie s neprečítanými príspevkami, do ktorého som prispel',
	'IMG_STICKY_UNREAD_LOCKED'		=> 'Zamknuté oznámenie s neprečítanými príspevkami',
	'IMG_STICKY_UNREAD_LOCKED_MINE'	=> 'Zamknuté s neprečítanými príspevkami, do ktorého som prispel',

	'IMG_ANNOUNCE_READ'					=> 'Dôležitá téma',
	'IMG_ANNOUNCE_READ_MINE'			=> 'Dôležitá téma, do ktorej som prispel',
	'IMG_ANNOUNCE_READ_LOCKED'			=> 'Zamknutá dôležitá téma',
	'IMG_ANNOUNCE_READ_LOCKED_MINE'		=> 'Zamknutá dôležitá téma, do ktorej som prispel',
	'IMG_ANNOUNCE_UNREAD'				=> 'Dôležitá téma s neprečítanými príspevkami',
	'IMG_ANNOUNCE_UNREAD_MINE'			=> 'Dôležitá téma s neprečítanými príspevkami, do ktorej som prispel',
	'IMG_ANNOUNCE_UNREAD_LOCKED'		=> 'Zamknutá dôležitá téma s neprečítanými príspevkami',
	'IMG_ANNOUNCE_UNREAD_LOCKED_MINE'	=> 'Zamknutá dôležitá téma s neprečítanými príspevkami, do ktorej som prispel',

	'IMG_GLOBAL_READ'					=> 'Globálna téma',
	'IMG_GLOBAL_READ_MINE'				=> 'Globálna téma, do ktorej som prispel',
	'IMG_GLOBAL_READ_LOCKED'			=> 'Zamknutá globálna téma',
	'IMG_GLOBAL_READ_LOCKED_MINE'		=> 'Zamknutá globálna téma, do ktorej som prispel',
	'IMG_GLOBAL_UNREAD'					=> 'Globálna téma s neprečítanými príspevkami',
	'IMG_GLOBAL_UNREAD_MINE'			=> 'Globálna téma s neprečítanými príspevkami, do ktorej som prispel',
	'IMG_GLOBAL_UNREAD_LOCKED'			=> 'Zamknutá globálna téma s neprečítanými príspevkami',
	'IMG_GLOBAL_UNREAD_LOCKED_MINE'		=> 'Zamknutá globálna téma s neprečítanými príspevkami, do ktorej som prispel',

	'IMG_PM_READ'		=> 'Prečítaná súkromná správa',
	'IMG_PM_UNREAD'		=> 'Neprečítaná súkromná správa',

	'IMG_ICON_BACK_TOP'		=> 'Nahor',

	'IMG_ICON_CONTACT_AIM'		=> 'AIM',
	'IMG_ICON_CONTACT_EMAIL'	=> 'Odoslať e-mailovú správu',
	'IMG_ICON_CONTACT_ICQ'		=> 'ICQ',
	'IMG_ICON_CONTACT_JABBER'	=> 'Jabber',
	'IMG_ICON_CONTACT_MSNM'		=> 'MSNM',
	'IMG_ICON_CONTACT_PM'		=> 'Odoslať správu',
	'IMG_ICON_CONTACT_YAHOO'	=> 'YIM',
	'IMG_ICON_CONTACT_WWW'		=> 'Webová stránka',

	'IMG_ICON_POST_DELETE'			=> 'Odstrániť príspevok',
	'IMG_ICON_POST_EDIT'			=> 'Upraviť príspevok',
	'IMG_ICON_POST_INFO'			=> 'Zobraziť detaily príspevku',
	'IMG_ICON_POST_QUOTE'			=> 'Citovať príspevok',
	'IMG_ICON_POST_REPORT'			=> 'Nahlásiť príspevok',
	'IMG_ICON_POST_TARGET'			=> 'Minipríspevok',
	'IMG_ICON_POST_TARGET_UNREAD'	=> 'Nový minipríspevok',


	'IMG_ICON_TOPIC_ATTACH'			=> 'Príloha',
	'IMG_ICON_TOPIC_LATEST'			=> 'Posledný príspevok',
	'IMG_ICON_TOPIC_NEWEST'			=> 'Posledný neprečítaný príspevok',
	'IMG_ICON_TOPIC_REPORTED'		=> 'Nahlásený príspevok',
	'IMG_ICON_TOPIC_UNAPPROVED'		=> 'Neschválený príspevok',

	'IMG_ICON_USER_ONLINE'		=> 'Prítomný používateľ',
	'IMG_ICON_USER_OFFLINE'		=> 'Neprítomný používateľ',
	'IMG_ICON_USER_PROFILE'		=> 'Zobraziť profil',
	'IMG_ICON_USER_SEARCH'		=> 'Vyhľadať príspevky',
	'IMG_ICON_USER_WARN'		=> 'Varovať používateľa',

	'IMG_BUTTON_PM_FORWARD'		=> 'Preposlať súkromnú správu',
	'IMG_BUTTON_PM_NEW'			=> 'Nová súkromná správa',
	'IMG_BUTTON_PM_REPLY'		=> 'Odpovedať na súkromnú správu',
	'IMG_BUTTON_TOPIC_LOCKED'	=> 'Zamknúť tému',
	'IMG_BUTTON_TOPIC_NEW'		=> 'Nová téma',
	'IMG_BUTTON_TOPIC_REPLY'	=> 'Odpovedať na tému',

	'IMG_USER_ICON1'		=> 'Používateľom definovaný obrázok 1',
	'IMG_USER_ICON2'		=> 'Používateľom definovaný obrázok 2',
	'IMG_USER_ICON3'		=> 'Používateľom definovaný obrázok 3',
	'IMG_USER_ICON4'		=> 'Používateľom definovaný obrázok 4',
	'IMG_USER_ICON5'		=> 'Používateľom definovaný obrázok 5',
	'IMG_USER_ICON6'		=> 'Používateľom definovaný obrázok 6',
	'IMG_USER_ICON7'		=> 'Používateľom definovaný obrázok 7',
	'IMG_USER_ICON8'		=> 'Používateľom definovaný obrázok 8',
	'IMG_USER_ICON9'		=> 'Používateľom definovaný obrázok 9',
	'IMG_USER_ICON10'		=> 'Používateľom definovaný obrázok 10',

	'INCLUDE_DIMENSIONS'		=> 'Zahrnúť rozmery',
	'INCLUDE_IMAGESET'			=> 'Zahrnúť sadu obrázkov',
	'INCLUDE_TEMPLATE'			=> 'Zahrnúť šablónu',
	'INCLUDE_THEME'				=> 'Zahrnúť tému',
	'INSTALL_IMAGESET'			=> 'Nainštalovať sadu obrázkov',
	'INSTALL_IMAGESET_EXPLAIN'	=> 'Tu sa dá nainštalovať sada obrázkov, ktorú ste vybrali. Môžete upresniť vaše nastavenie alebo použiť predvolené z inštalácie.',
	'INSTALL_STYLE'				=> 'Nainštalovať štýl',
	'INSTALL_STYLE_EXPLAIN'		=> 'Tu sa dá nainštalovať vybraný štýl a odpovedajúce položky a súčasti, pokiaľ sú potrebné. Pokiaľ už máte potrebné súčasti štýlov nainštalované, nebudú prepísané. Niektoré štýly vyžadujú, aby ich súčasti boli nainštalované vopred. Budete upozornený, pokiaľ by ste sa pokúsili taký štýl nainštalovať bez potrebných súčastí.',
	'INSTALL_TEMPLATE'			=> 'Nainštalovať šablónu',
	'INSTALL_TEMPLATE_EXPLAIN'	=> 'Tu sa dá nainštalovať šablóna, ktorú ste vybrali. Podľa nastavení servera a oprávnení k súborom vám tu budú ponúknuté rôzne možnosti nastavení.',
	'INSTALL_THEME'				=> 'Nainštalovať tému',
	'INSTALL_THEME_EXPLAIN'		=> 'Tu sa dá nainštalovať téma, ktorý ste vybrali. Môžete upresniť vaše nastavenie alebo použiť predvolené z inštalácie.',
	'INSTALLED_IMAGESET'		=> 'Nainštalované sady obrázkov',
	'INSTALLED_STYLE'			=> 'Nainštalované štýly',
	'INSTALLED_TEMPLATE'		=> 'Nainštalované šablóny',
	'INSTALLED_THEME'			=> 'Nainštalované témy',

	'LINE_SPACING'				=> 'Medzery medzi riadkami',
	'LOCALISED_IMAGES'			=> 'Lokalizované obrázky',

	'NO_CLASS'					=> 'Nedá sa nájsť trieda v štýloch',
	'NO_IMAGESET'				=> 'Nedá sa nájsť sada obrázkov v súboroch.',
	'NO_IMAGE'					=> 'Bez obrázka',
	'NO_IMAGE_ERROR'			=> 'Nedá sa nájsť obrázok v systéme súborov.',
	'NO_STYLE'					=> 'Nedá sa nájsť štýl v súboroch.',
	'NO_TEMPLATE'				=> 'Nedá sa nájsť šablóna v súboroch.',
	'NO_THEME'					=> 'Nedá sa nájsť téma v súboroch.',
	'NO_UNINSTALLED_IMAGESET'	=> 'Žiadne odinštalované sady obrázkov',
	'NO_UNINSTALLED_STYLE'		=> 'Žiadne odinštalované štýly',
	'NO_UNINSTALLED_TEMPLATE'	=> 'Žiadne odinštalované šablóny',
	'NO_UNINSTALLED_THEME'		=> 'Žiadne odinštalované témy',
	'NO_UNIT'					=> 'Žiadne',

	'ONLY_IMAGESET'			=> 'Toto je posledná sada obrázkov, nemôžete ju odstrániť.',
	'ONLY_STYLE'			=> 'Toto je posledný štýl, nemôžete ho odstrániť.',
	'ONLY_TEMPLATE'			=> 'Toto je posledná šablóna, nemôžete ju odstrániť.',
	'ONLY_THEME'			=> 'Toto je posledná téma, nemôžete ju odstrániť.',
	'OPTIONAL_BASIS'		=> 'Voliteľné',

	'REFRESH'					=> 'Obnoviť',
	'REPEAT_NO'					=> 'Žiadne',
	'REPEAT_X'					=> 'Len horizontálne',
	'REPEAT_Y'					=> 'Len vertikálne',
	'REPEAT_ALL'				=> 'Obidvoma smermi',
	'REPLACE_IMAGESET'			=> 'Nahradiť sadu obrázkov',
	'REPLACE_IMAGESET_EXPLAIN'	=> 'Vybraná sada obrázkov nahradí odstraňovanú vo všetkých štýloch, kde je použitá.',
	'REPLACE_STYLE'				=> 'Nahradiť štýl',
	'REPLACE_STYLE_EXPLAIN'		=> 'Vybraný štýl nahradí ten odstraňovaný pre všetkých používateľov, ktorí ho používajú.',
	'REPLACE_TEMPLATE'			=> 'Nahradiť šablónu',
	'REPLACE_TEMPLATE_EXPLAIN'	=> 'Vybraná šablóna nahradí odstraňovanú vo všetkých štýloch, kde je použitá.',
	'REPLACE_THEME'				=> 'Nahradiť tému',
	'REPLACE_THEME_EXPLAIN'		=> 'Vybraná téma nahradí odstraňovanú vo všetkých štýloch, kde je použitá.',
	'REQUIRES_IMAGESET'			=> 'Tento štýl vyžaduje, aby sada šablón %s bola už nainštalovaná.',
	'REQUIRES_TEMPLATE'			=> 'Tento štýl vyžaduje, aby sada obrázkov %s bola už nainštalovaná.',
	'REQUIRES_THEME'			=> 'Tento štýl vyžaduje, aby téma %s bola už nainštalovaný.',

	'SELECT_IMAGE'				=> 'Vyberte obrázok',
	'SELECT_TEMPLATE'			=> 'Vyberte súbor šablóny',
	'SELECT_THEME'				=> 'Vybrať súbor témy',
	'SELECTED_IMAGE'			=> 'Vybraný obrázok',
	'SELECTED_IMAGESET'			=> 'Vybraná sada obrázkov',
	'SELECTED_TEMPLATE'			=> 'Vybraná šablóna',
	'SELECTED_TEMPLATE_FILE'	=> 'Vybraný súbor šablóny',
	'SELECTED_THEME'			=> 'Vybraná téma',
	'SELECTED_THEME_FILE'		=> 'Vybraný súbor témy',
	'STORE_DATABASE'			=> 'Databáza',
	'STORE_FILESYSTEM'			=> 'Súborový systém',
	'STYLE_ACTIVATE'			=> 'Aktivovať',
	'STYLE_ACTIVE'				=> 'Aktívny',
	'STYLE_ADDED'				=> 'Štýl bol úspešne pridaný.',
	'STYLE_DEACTIVATE'			=> 'Deaktivovať',
	'STYLE_DEFAULT'				=> 'Označiť ako predvolený štýl',
	'STYLE_DELETED'				=> 'Štýl bol úspešne odstránený.',
	'STYLE_DETAILS_UPDATED'		=> 'Štýl bol úspešne aktualizovaný.',
	'STYLE_ERR_ARCHIVE'			=> 'Prosím, vyberte archivačnú metódu.',
	'STYLE_ERR_COPY_LONG'		=> 'Copyright nemôže byť dlhší ako 60 znakov.',
	'STYLE_ERR_MORE_ELEMENTS'	=> 'Musíte vybrať aspoň jednu súčasť štýlu.',
	'STYLE_ERR_NAME_CHARS'		=> 'Názov štýlu môže obsahovať len alfanumerické znaky, -, +, _ a medzery.',
	'STYLE_ERR_NAME_EXIST'		=> 'Štýl s týmto názvom už existuje.',
	'STYLE_ERR_NAME_LONG'		=> 'Názov štýlov nesmie byť dlhší ako 30 znakov.',
	'STYLE_ERR_NO_IDS'			=> 'Pre tento štýl musíte vybrať tému, šablónu a sadu obrázkov.',
	'STYLE_ERR_NOT_STYLE'		=> 'Importovaný alebo odoslaný archív neobsahoval platný štýl.',
	'STYLE_ERR_STYLE_NAME'		=> 'Musíte zvoliť názov pre tento štýl.',
	'STYLE_EXPORT'				=> 'Exportovať štýl',
	'STYLE_EXPORT_EXPLAIN'		=> 'Tu môžete exportovať štýl do archívu. Štýl nemusí obsahovať všetky prvky, ale najmenej jeden. Napríklad pokiaľ ste vytvorili novú tému a sadu obrázkov pre často používanú šablónu, môžete exportovať len tému a sadu obrázkov a šablónu vynechať. Môžete si vybrať, či chcete súbor stiahnuť priamo alebo ho uložiť na serveri na neskoršie stiahnutie.',
	'STYLE_EXPORTED'			=> 'Štýl bol úspešne exportovaný a uložený v %s.',
	'STYLE_IMAGESET'			=> 'Sada obrázkov',
	'STYLE_NAME'				=> 'Názov štýlu',
	'STYLE_TEMPLATE'			=> 'Šablóna',
	'STYLE_THEME'				=> 'Téma',
	'STYLE_USED_BY'				=> 'Počet používateľov (vrátane robotov)',

	'TEMPLATE_ADDED'			=> 'Sada šablón pridaná a uložená v súborovom systéme.',
	'TEMPLATE_ADDED_DB'			=> 'Sada šablón pridaná a uložená v databáze.',
	'TEMPLATE_CACHE'			=> 'Vyrovnávacia pamäť šablón',
	'TEMPLATE_CACHE_EXPLAIN'	=> 'phpBB ukladá kópie šablón do vyrovnávacej pamäte. Toto znižuje zaťaženie servera a dobu načítania zakaždým, keď je na fóre načítaná akákoľvek stránka. Tu si môžete prezrieť stav všetkých súborov vo vyrovnávacej pamäti, prípadne z nej odstrániť jeden alebo viac súborov.',
	'TEMPLATE_CACHE_CLEARED'	=> 'Priečinok pre vyrovnávaciu pamäť šablón bol úspešne prečistený.',
	'TEMPLATE_CACHE_EMPTY'		=> 'Vo vyrovnávacej pamäti nie sú uložené žiadne šablóny.',
	'TEMPLATE_DELETED'			=> 'Sada šablón bola úspešne odstránená.',
	'TEMPLATE_DELETED_FS'		=> 'Sada šablón bola úspešne odstránená z databázy, ale na serveri mohlo zostať niekoľko súborov zo sady.',
	'TEMPLATE_DETAILS_UPDATED'	=> 'Podrobnosti o šablóne boli úspešne aktualizované.',
	'TEMPLATE_EDITOR'			=> 'HTML editor šablón',
	'TEMPLATE_EDITOR_HEIGHT'	=> 'Výška editora šablón',
	'TEMPLATE_ERR_ARCHIVE'		=> 'Prosím, zvoľte archivačnú metódu.',
	'TEMPLATE_ERR_CACHE_READ'	=> 'Priečinok pre vyrovnávaciu pamäť, ktorý slúži pre urýchlenie načítania šablón, nemohol byť otvorený.',
	'TEMPLATE_ERR_COPY_LONG'	=> 'Copyright nesmie byť dlhší ako 60 znakov.',
	'TEMPLATE_ERR_NAME_CHARS'	=> 'Názov šablóny môže obsahovať len alfanumerické znaky -, +, _ a medzeru.',
	'TEMPLATE_ERR_NAME_EXIST'	=> 'Sada šablón s týmto názvom už existuje.',
	'TEMPLATE_ERR_NAME_LONG'	=> 'Názov šablóny nesmie byť dlhší ako 60 znakov.',
	'TEMPLATE_ERR_NOT_TEMPLATE'	=> 'Zadaný archív neobsahuje platnú sadu šablón.',
	'TEMPLATE_ERR_STYLE_NAME'	=> 'Musíte zadať názov pre túto šablónu.',
	'TEMPLATE_EXPORT'			=> 'Exportovať šablóny',
	'TEMPLATE_EXPORT_EXPLAIN'	=> 'Tu môžete exportovať sadu šablón do archívu. Tento archív bude obsahovať všetky potrebné údaje pre inštaláciu sady šablón na inom fóre. Môžete si vybrať, či chcete súbor stiahnuť priamo alebo ho uložiť na serveri pre neskoršie stiahnutie.',
	'TEMPLATE_EXPORTED'			=> 'Šablóna úspešne exportovaná a uložená v %s.',
	'TEMPLATE_FILE'				=> 'Súbor šablóny',
	'TEMPLATE_FILE_UPDATED'		=> 'Súbor šablóny bol úspešne aktualizovaný.',
	'TEMPLATE_LOCATION'			=> 'Ukladať šablóny v',
	'TEMPLATE_LOCATION_EXPLAIN'	=> 'Obrázky budú vždy ukladané v súborovom systéme.',
	'TEMPLATE_NAME'				=> 'Názov šablóny',
	'TEMPLATE_REFRESHED'		=> 'Šablóna bola úspešne aktualizovaná.',

	'THEME_ADDED'				=> 'Nová téma bola úspešne pridaná do databázy.',
	'THEME_ADDED_DB'			=> 'Nová téma bola úspešne pridaná do databázy.',
	'THEME_CLASS_ADDED'			=> 'Vlastná trieda bola úspešne pridaná.',
	'THEME_DELETED'				=> 'Téma bola úspešne odstránená.',
	'THEME_DELETED_FS'			=> 'Téma bola úspešne odstránená z databázy, ale na serveri mohlo zostať niekoľko súborov témy.',
	'THEME_DETAILS_UPDATED'		=> 'Detaily témy boli úspešne aktualizované.',
	'THEME_EDITOR'				=> 'CSS editor skinov',
	'THEME_EDITOR_HEIGHT'		=> 'Veľkosť editora skinov.',
	'THEME_ERR_ARCHIVE'			=> 'Prosím, vyberte archivačnú metódu.',
	'THEME_ERR_CLASS_CHARS'		=> 'V názvoch triedy môžu byť len alfanumerické znaky ., :, -, _ a #.',
	'THEME_ERR_COPY_LONG'		=> 'Copyright nesmie byť dlhší ako 60 znakov',
	'THEME_ERR_NAME_CHARS'		=> 'Názov skinu môže obsahovať len alfanumerické znaky, -, +, _ a medzery.',
	'THEME_ERR_NAME_EXIST'		=> 'Téma s týmto názvom už existuje.',
	'THEME_ERR_NAME_LONG'		=> 'Názov témy nesmie byť dlhší ako 30 znakov.',
	'THEME_ERR_NOT_THEME'		=> 'Importovaný alebo odoslaný archív neobsahoval platnú tému.',
	'THEME_ERR_REFRESH_FS'		=> 'Táto téma je uložená v súboroch a preto nie je potrebné ju obnovovať.',
	'THEME_ERR_STYLE_NAME'		=> 'Musíte zvoliť názov pre túto tému.',
	'THEME_FILE'				=> 'Súbor témy',
	'THEME_EXPORT'				=> 'Exportovať tému',
	'THEME_EXPORT_EXPLAIN'		=> 'Tu môžete exportovať tému do archívu. Tento archív bude obsahovať všetky potrebné údaje pre inštaláciu témy na inom fóre. Môžete si vybrať, či chcete súbor stiahnuť priamo alebo ho uložiť na serveri pre neskoršie stiahnutie.',
	'THEME_EXPORTED'			=> 'Téma bola úspešne exportovaná a uložená v %s.',
	'THEME_LOCATION'			=> 'Ukladať štýly v',
	'THEME_LOCATION_EXPLAIN'	=> 'Obrázky sú vždy ukladané v súboroch.',
	'THEME_NAME'				=> 'Názov témy',
	'THEME_REFRESHED'			=> 'Téma bola úspešne obnovená.',
	'THEME_UPDATED'				=> 'Téma bola úspešne aktualizovaná.',

	'UNDERLINE'				=> 'Podčiarknuté',
	'UNINSTALLED_IMAGESET'	=> 'Nenainštalované sady obrázkov',
	'UNINSTALLED_STYLE'		=> 'Nenainštalované štýly',
	'UNINSTALLED_TEMPLATE'	=> 'Nenainštalované šablóny',
	'UNINSTALLED_THEME'		=> 'Nenainštalované témy',
	'UNSET'					=> 'Nedefinované',

));

?>
