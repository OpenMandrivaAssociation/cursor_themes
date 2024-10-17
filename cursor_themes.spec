%define name    cursor_themes

%define version 0.0.5
%define release 9

Summary:	A Collection of cursor themes for XFree86 4.3 or later
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		https://kde-look.org
BuildArch:	noarch
Group:		Graphical desktop/Other
Source:		choose_cursor
Source1:        4805-RedDot.tar.bz2
Source2:        4858-YCursors.tar.bz2
Source3:        4975-GKD-XCursors.tar.bz2
Source5:        5076-corp.tar.bz2
Source6:        5077-innerspace.tar.bz2
Source7:        5078-vox.tar.bz2
%define		bexos_ver		0.4
Source8:        5211-bexos_color_%{bexos_ver}.tar.bz2
Source9:        5238-3dwhite.tar.bz2
Source10:       5265-3Dcursors-0.2.tar.bz2
Source11:       5271-3dcolor.tar.bz2
Source12:       5359-tuxcursor02.tar.gz
Source13:       5376-tuxcute.tar.bz2
Source14:       5376-tuxresize.tar.bz2
Source15:       5475-yellowdot.tar.bz2
Source16:       5507-Golden-XCursors-3D-0.8.tar.bz2
Source17:       5532-BlueGlass-XCursors-3D-0.4.tar.bz2
Source18:       5533-Silver-XCursors-3D-0.4.tar.bz2
Source19:	5600-redhat9cursor.tar.bz2
Source20:	5605-cursor_mix.tar.bz2
Source21:	5833-aquadiz.tar.bz2
Source22:	6132-SignalOS-Cursors-0.0.2.tar.bz2
Source23:	6240-crystalcursors.tar.bz2
Source24:	6277-bean.tar.bz2
Source25:	6336-flat_white_cursor_0.3.tar.bz2
Source26:	6504-flat_black_cursor_0.3.tar.bz2
Source27:	6550-Jimmac.tar.bz2
Source28:	macoscursors-default-0.2.tar.bz2
Source29:	tuxsplash.tar.bz2
Source30:	10394-justwhite-0.2.tar.bz2
Source31:	10500-justgreen-0.1a.tar.bz2
Source32:	10163-justblue-0.21.tar.bz2
Source33:	10211-daliesque.tar.bz2
Source34:	11313-pearlgrey-1.0.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}
Requires:	gtkdialogs
Requires:	XFree86 >= 4.3
BuildRequires:	imagemagick XFree86 >= 4.3
Prefix:		%{_prefix}

%description
This package contains all the freely distributeable cursor themes for XFree86
4.3 or newer currently available from http://kde-look.org, along with a 
simple script (choose_cursor) which will allow you to easily choose a 
cursor theme.

%prep
#rm -rf $RPM_BUILD_ROOT
%setup -T -c -q -a 1 -a 2 -a 3 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 20 -a 21 -a 22 -a 23 -a 24 -a 27 -a 28 -a 29 -a 30 -a 31 -a 32 -a 33 -a 34
tar -xzf tuxshadow.tar.gz
mv tuxcursor tuxshadow
tar -xzf tuxcursor.tar.gz
mv tuxcursor tuxcursor.orig
tar xjf %{SOURCE13}; mv tuxcursor tuxcute
tar xjf %{SOURCE14}; mv tuxcursor tuxresize
mv tuxcursor.orig tuxcursor
tar xjf %{SOURCE19}; mkdir redhat;mv cursors redhat
tar xjf %{SOURCE25}; mkdir flat_white;mv cursors flat_white
tar xjf %{SOURCE26}; mkdir flat_black;mv cursors flat_black

%build
rm -Rf default
#pushd reddot;make;popd
mkdir -p GKD-XCursors/cursors;cp -f GKD-XCursors/* GKD-XCursors/cursors 2>/dev/null||:
rm -f GKD-XCursors/cursors/*.png
mkdir -p bexos_color_%{bexos_ver}/bexos_color/cursors;cp -f bexos_color_%{bexos_ver}/* bexos_color_%{bexos_ver}/bexos_color/cursors 2>/dev/null||:
#pushd maccursors; rm -f crosshair cross_reverse hand1 hand2;popd

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m755 %{SOURCE0} %{buildroot}/%{_bindir}


#Menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=Cursor Themes
Comment=Choose a Cursor Theme
Exec=choose_cursor
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;DesktopSettings;
EOF

mkdir -p %{buildroot}/{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
install -m644 RedDotSource/sources/hand.png %{buildroot}/%{_iconsdir}/%{name}.png
convert -resize 16x16 RedDotSource/sources/hand.png %{buildroot}/%{_miconsdir}/%{name}.png
convert -resize 48x48 RedDotSource/sources/hand.png %{buildroot}/%{_liconsdir}/%{name}.png
pwd
CURSORS=`find . -type d -name 'cursors'`
echo -e "\n\n\n\t\tFound the following cursors:\n $CURSORS\n\n\n"
set +x
for CURSOR in $CURSORS
	do CURSORNAME=$(basename `dirname $CURSOR`)
	CURSORNAME=${CURSORNAME%%-*[0-9]*}
	if [ "$CURSORNAME" == "*-[0-9]*" ]
	then echo "$CURSORNAME is versioned" >&2; CURSORNAME=${CURSORNAME#-[0-9]*}
	fi
	mkdir -p %{buildroot}/%{_iconsdir}/$CURSORNAME
	cp -a $CURSOR %{buildroot}/%{_iconsdir}/$CURSORNAME

	#Ensure links are in place:
	pushd %{buildroot}/%{_iconsdir}/$CURSORNAME/cursors >/dev/null

	
	[ -e hand -a ! -f hand1 ] && ln -sf hand hand1 >/dev/null 2>&1||:
	[ -e hand -a ! -f hand2 ] && ln -sf hand hand2 >/dev/null 2>&1||:
	[ -e cross -a ! -f crosshair ] && ln -sf cross crosshair >&- 2>&- ||:
	[ -e cross -a ! -f cross_reverse ] && ln -sf cross cross_reverse >&- 2>&- ||:

	#QT symlinks mess :-(
	[ -e v_double_arrow ] && ln -sf v_double_arrow	00008160000006810000408080010102 #v_double_arrow
	[ -e h_double_arrow ] && ln -sf h_double_arrow	028006030e0e7ebffc7f7070c0600140 #h_double_arrow
	[ -e fd_double_arrow ] && ln -sf fd_double_arrow	fcf1c3c7cd4491d801f1e1c78f100000 #fd_double_arrow
	[ -e bd_double_arrow ] && ln -sf bd_double_arrow	c7088f0f3e6c8088236ef8e1e3e70000 #bd_double_arrow
	[ -e sb_h_double_arrow ] && ln -sf sb_h_double_arrow   14fef782d02440884392942c11205230 #sb_h_double_arrow
	[ -e sb_v_double_arrow ] && ln -sf sb_v_double_arrow   2870a09082c103050810ffdffffe0204 #sb_v_double_arrow
	[ -e hand1 ] && ln -sf hand1 9d800788f1b08800ae810202380a0822 #hand1
	[ -e hand2 ] && ln -sf hand2 e29285e634086352946a0e7090d73106 #hand2
	[ -e crossed_circle ] && ln -sf crossed_circle 03b6e0fcb3499374a867c041f52298f0 #crossed_circle (dnd forbidden)
	[ -e move ] && ln -sf move 4498f0e0c1937ffe01fd06f973665830 #left_ptr (move_cursor)
	[ -e copy ] && ln -sf copy 6407b0e94181790501fd1e167b474872 #copy
	[ -e link ] && ln -sf link 640fb0e74195791501fd1ed57b41487f # link
	[ -e left_ptr_watch ] && ln -sf left_ptr_watch 3ecb610c1bf2410f44200f48c40d3599 # left_ptr_watch
	[ -e question_arrow ] && ln -sf question_arrow d9ce0ab605698f320427677b458ad60b # question_arrow
	
	#Other apps' symlinks
	[ -e left_ptr_watch ] && ln -sf left_ptr_watch 08e8e1c95fe2fc01f976f1e063a24ccd #mozilla's left_ptr_watch
	popd >/dev/null
done
set -x

pushd %{buildroot}/%{_iconsdir}/ ; ln -s RedDot reddot;popd
rm -Rf %{buildroot}/%{_iconsdir}/RedDotSource

echo "%defattr(-,root,root)" > %name.files
find %{buildroot}/%{_datadir}/icons/ -type d -o -type l -maxdepth 1 -mindepth 1|egrep -v "(large|mini)"|sed -e 's|%{buildroot}/||;s|%{_datadir}|%%{_datadir}|'|sort>> %name.files

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ "$1" = "2" -a -d %{_datadir}/icons/reddot ]; then
 rm -rf %{_datadir}/icons/reddot
fi

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %name.files
%defattr(-,root,root)
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_bindir}/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.5-8mdv2011.0
+ Revision: 617483
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.0.5-7mdv2010.0
+ Revision: 425448
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.0.5-6mdv2009.0
+ Revision: 243833
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.0.5-4mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Funda Wang <fwang@mandriva.org> 0.0.5-4mdv2008.0
+ Revision: 73449
- fix menu category -> Only Settings/DesktopSettings now.

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.0.5-3mdv2008.0
+ Revision: 69492
- convert menu to XDG
- use %%mkrel


* Tue Aug 17 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.0.5-2mdk
- Add script to fix upgrade (Mdk bug #10316)

* Mon Apr 19 2004 Buchan Milne <bgmilne@linux0mandrake.com> 0.0.5-1mdk
- Fixes to choose-cursor
   -Fix support for zenity's gdialog (really better fix for chatty kdialog)
     fixes #9455
   -Prevent themes ever getting version numbers
   -Ensure we really get user icons
- Cursor theme update
   -Updates: RedDot (keep link to reddot)
   -New themes: justwhite,justgreen,justwhite,daliesque

* Wed Aug 27 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.0.4-1mdk
- Fixes in script:
  - Fixes for chatty kdialog (don't redirect stderr to stdout), but
    don't break cdialog support (outputs choice to stderr)
  - Tell the user if we don't have a usable dialog program
  - Don't use gdialog in console (zenity gdialog doesn't work in
    console)
  - Adjust dialog sizes to fit for cdialog
- Since we have gmessage warning if no dialog is found, don't require a
  dialog, just gtkdialogs (for gmessage)
- Don't use versions in theme name

* Wed Jul 16 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.0.3-1mdk
- Fixes in script
- 11i or more new cursor themes, and 3 updated themes
- Own theme directories (distriblint)
- Drop Xdialog requirement, and hope the user has a dialog program (is there a
  better solution?)

* Sun Apr 06 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.0.2-2mdk
- Fixes to choose_cursor (thanks Duncan)
- bexos_colour 0.4, BlueGlass 0.2
- Fix up bexos so we actually include it
- Untar tuxcursors so we include them too

* Thu Apr 03 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.0.2-1mdk
- New choose_cursor script

* Sun Mar 30 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.0.1-2mdk
- BuildRequires (thx sldb)

* Sat Mar 29 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.0.1-1mdk
- First Mandrake package (25 total cursor themes besides the 3 stock ones)

