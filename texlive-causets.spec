%global tl_name causets
%global tl_revision 74247

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Draw causal set (Hasse) diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/causets
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/causets.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/causets.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package uses TikZ to generate (Hasse) diagrams for causal
sets (causets) to be used inline with text or in mathematical
expressions. The macros can also be used in the tikzpicture environment
to annotate or modify a diagram, as shown with some examples in the
documentation.

