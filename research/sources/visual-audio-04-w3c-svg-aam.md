Source: https://www.w3.org/TR/svg-aam-1.0/
Title: SVG Accessibility API Mappings
Fetched: 2026-11-12T03:01:23.150Z

[↑Jump to Table of Contents](https://www.w3.org/TR/svg-aam-1.0/#toc) [←Collapse Sidebar](https://www.w3.org/TR/svg-aam-1.0/#toc)![](https://www.w3.org/StyleSheets/TR/2021/logos/dark.svg)lightdarkauto

[![W3C](https://www.w3.org/StyleSheets/TR/2021/logos/W3C)](https://www.w3.org/)

# SVG Accessibility API Mappings

[W3C Working Draft](https://www.w3.org/standards/types#WD) 21 October 2026

More details about this documentThis version:[https://www.w3.org/TR/2026/WD-svg-aam-1.0-20261021/](https://www.w3.org/TR/2026/WD-svg-aam-1.0-20261021/)Latest published version:[https://www.w3.org/TR/svg-aam-1.0/](https://www.w3.org/TR/svg-aam-1.0/)Latest editor's draft:[https://w3c.github.io/aria/svg-aam/](https://w3c.github.io/aria/svg-aam/)History:[https://www.w3.org/standards/history/svg-aam-1.0/](https://www.w3.org/standards/history/svg-aam-1.0/)[Commit history](https://github.com/w3c/aria/commits/main/svg-aam/)
Editors:
[Cynthia Shelly](mailto:buphie@gmail.com) (Invited Expert)
[Mark Rogers](mailto:mark.rogers@powermapper.com) (PowerMapper)

Former editors:
[Amelia Bellamy-Royds](mailto:amelia.bellamy.royds@gmail.com) (Invited Expert)
[Ian Pouncey](mailto:w3c@ipouncey.co.uk) ( [The Paciello Group, LLC](https://www.paciellogroup.com/))

Authors:
[Amelia Bellamy-Royds](mailto:amelia.bellamy.royds@gmail.com) (Invited Expert)
[Ian Pouncey](mailto:w3c@ipouncey.co.uk) ( [The Paciello Group, LLC](https://www.paciellogroup.com/))
[Richard Schwerdtfeger](mailto:richschwer@gmail.com) ( [Knowbility](https://knowbility.org/)) (until August 2017)
[Doug Schepers](mailto:schepers@w3.org) ( [W3C](https://www.w3.org/)) (until December 2016)
Feedback:[GitHub w3c/svg-aam](https://github.com/w3c/svg-aam/)
( [pull requests](https://github.com/w3c/aria/pulls?q=is%3Apr+is%3Aopen+label%3A%22spec%3Asvg-aam%22),
[new issue](https://github.com/w3c/svg-aam/issues/new/choose),
[open issues](https://github.com/w3c/svg-aam/issues/))


[Copyright](https://www.w3.org/policies/#copyright)
©
2015-2026

[World Wide Web Consortium](https://www.w3.org/).
W3C® [liability](https://www.w3.org/policies/#Legal_Disclaimer),
[trademark](https://www.w3.org/policies/#W3C_Trademarks) and
[permissive document license](https://www.w3.org/copyright/software-license-2023/ "W3C Software and Document Notice and License") rules apply.


* * *

## Abstract

SVG Accessibility API Mappings (SVG-AAM) defines how [user agents](https://infra.spec.whatwg.org/#user-agent) map Scalable Vector Graphics (SVG) \[[SVG2](https://www.w3.org/TR/svg-aam-1.0/#bib-svg2 "Scalable Vector Graphics (SVG) 2")\] markup to platform
[accessibility application programming interfaces (APIs)](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api). It is intended for SVG user
agent developers responsible for SVG accessibility in their user agent.


This specification allows SVG authors to create accessible rich internet applications, including charts, graphs, and other drawings. It does this by extending the
[Core Accessibility API Mappings 1.1](https://www.w3.org/TR/core-aam-1.1/) (CORE-AAM) \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\] and the
[Accessible Name and Description: Computation and API Mappings 1.1](https://www.w3.org/TR/accname-1.1/) (ACCNAME-AAM) \[[ACCNAME-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-accname-aam "Accessible Name and Description Computation 1.1")\] specifications for user agents. It
leverages those core mappings and provides SVG-specific guidance to define how the SVG user agent must respond to keyboard focus and [role](https://www.w3.org/TR/wai-aria-1.3/#dfn-role), [state](https://www.w3.org/TR/wai-aria/#dfn-state) and [property](https://www.w3.org/TR/wai-aria/#dfn-property) attributes
provided in Web content via
[WAI-ARIA](https://www.w3.org/TR/wai-aria-1.1/)
\[[WAI-ARIA](https://www.w3.org/TR/svg-aam-1.0/#bib-wai-aria "Accessible Rich Internet Applications (WAI-ARIA) 1.1")\]. The SVG-AAM also adapts the ACCNAME-AAM to make use of standard SVG features used to compute accessible names and description information exposed by platform accessibility
APIs.


The SVG-AAM is part of the
WAI-ARIA suite described in the
[WAI-ARIA Overview](https://www.w3.org/WAI/intro/aria.php).


## Status of This Document

_This section describes the status of this_
_document at the time of its publication. A list of current W3C_
_publications and the latest revision of this technical report can be found_
_in the_
_[W3C standards and drafts index](https://www.w3.org/TR/)._

Note

We are in the process of updating this spec to align with changes in SVG 2.0. This is an early draft that contains outdated information and errors. Please do not implement based on this draft.


To comment, [file an issue in the SVG AAM GitHub repository](https://github.com/w3c/svg-aam/issues/new). Create a separate GitHub issue for each topic, rather than commenting on
multiple topics in a single issue. It is free to create a GitHub account to file issues. Before commenting, please first review the SVG AAM GitHub repository for related comments. If filing
issues in GitHub is not feasible, email [public-svg-a11y@w3.org](mailto:public-svg-a11y@w3.org) ( [mail archive of previous comments](https://lists.w3.org/Archives/Public/public-svg-a11y/)).


Particularly problematic open issues are highlighted in this document, with links to the GitHub discussion. Comments on these issues would be particularly appreciated.

Relative to the last published working draft (10 May 2018), the following changes have been made:

- Removal of a number of SVG elements that are either deprecated or no longer present in the SVG 2 Editor's Draft. These include:

  - audio
  - canvas
  - cursor
  - discard
  - hatch
  - hatchpath
  - iframe
  - mesh
  - meshpatch
  - meshrow
  - solidcolor
  - source
  - track
  - video

Relative to the previously published Working Draft (8 September 2016), the following major changes have been made:

- The handling of `use` element shadow DOM content has changed.
- The roles for determining whether an element is hidden have been simplified, and coordinated with changes to other WAI-ARIA specifications.

In addition, there have been numerous clarifying edits.

This document was initially developed jointly by the [Accessible Rich Internet Applications Working Group](https://www.w3.org/groups/wg/aria/) and the
[SVG Working Group](https://www.w3.org/groups/wg/svg/), through the
[SVG Accessibility Task Force](https://www.w3.org/groups/tf/svg-a11y/). It is now produced by the ARIA Working Group in coordination
with other specifications developed by the ARIA and SVG Working Groups.


This document was published by the [Accessible Rich Internet Applications Working Group](https://www.w3.org/groups/wg/aria) as
a Working Draft using the
[Recommendation\\
track](https://www.w3.org/policies/process/20250818/#recs-and-notes).


Publication as
a Working Draft does not imply endorsement
by W3C and its Members.

This is a draft document and may be updated, replaced, or obsoleted by other
documents at any time. It is inappropriate to cite this document as other
than a work in progress.




This document was produced by a group
operating under the
[W3C Patent\\
Policy](https://www.w3.org/policies/patent-policy/).


W3C maintains a
[public list of any patent disclosures](https://www.w3.org/groups/wg/aria/ipr)
made in connection with the deliverables of
the group; that page also includes
instructions for disclosing a patent. An individual who has actual
knowledge of a patent that the individual believes contains
[Essential Claim(s)](https://www.w3.org/policies/patent-policy/#def-essential)
must disclose the information in accordance with
[section 6 of the W3C Patent Policy](https://www.w3.org/policies/patent-policy/#sec-Disclosure).



This document is governed by the
[18 August 2025 W3C Process Document](https://www.w3.org/policies/process/20250818/).


## 1\. Introduction

[Permalink for Section 1.](https://www.w3.org/TR/svg-aam-1.0/#intro)

_This section is non-normative._

This specification defines how SVG host language elements and content — with or without WAI-ARIA roles, states, and properties
applied — map to accessibility APIs. Sections give guidance on calculating text alternatives, mapping actions to
[events](https://dom.spec.whatwg.org/#concept-event), event processing, special document handling procedures, and error handling.


This introduction provides some background on why this specification exists, and how it relates to other WAI-ARIA specifications. It includes a general overview of accessibility
APIs and the hierarchy of [accessible objects](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) known as the
[accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree).


### 1.1 History and Purpose

[Permalink for Section 1.1](https://www.w3.org/TR/svg-aam-1.0/#intro_history)

In traditional Graphical User Interface (GUI) applications, components of the User Interface (UI) are displayed when needed and hidden when not needed based on user interactions.
[Accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) are used to communicate
[semantics](https://www.w3.org/TR/wai-aria/#dfn-semantics)
about the user interface to
[assistive technologies](https://www.w3.org/TR/wai-aria-1.3/#dfn-assistive-technologies)
used by people with disabilities.


These APIs constitute a contract between applications and assistive technologies, such as screen readers, magnifiers, alternate input
devices, and speech command and control, to enable them to access the appropriate semantics needed to produce a usable alternative to interactive applications or complex documents. For
example, screen-reading software for blind users can determine whether a particular UI component is a menu, button, text field, list box, etc. It can also
present the information in tables or lists in a way that provides context for each piece of text.


For web documents and applications, the essential semantic information is encapsulated within the Document Object Model (DOM). Assistive
technologies obtain this information from the [user agent](https://infra.spec.whatwg.org/#user-agent) (web browser), which maps elements and attributes to the platform Accessibility
API.


In Scalable Vector Graphics (SVG) documents, most SVG [elements](https://dom.spec.whatwg.org/#concept-element)
do not provide semantic information of value to assistive technologies. Instead, they represent low-level vector graphics drawing directives. That element only has meaning to assistive
technologies if the author provides alternative text, descriptions, or WAI-ARIA semantics.


Both version 1 \[[SVG1](https://www.w3.org/TR/svg-aam-1.0/#bib-svg1 "Scalable Vector Graphics (SVG) 1.0 Specification")\] and version 1.1 \[[SVG11](https://www.w3.org/TR/svg-aam-1.0/#bib-svg11 "Scalable Vector Graphics (SVG) 1.1 (Second Edition)")\] of the SVG specifications included elements for defining [accessible names](https://www.w3.org/TR/accname-1.1/#dfn-accessible-name) and
[descriptions](https://www.w3.org/TR/accname-1.1/#dfn-accessible-description) (`<title>` and `<desc>`). However, prior to this specification, there was no normative guidance as to
how user agents should expose this information to assistive technologies, or how to integrate it with host languages and validators that support WAI-ARIA. There was similarly no guidance on
how user agents should make interactive SVG [keyboard accessible](https://www.w3.org/TR/wai-aria-1.3/#dfn-keyboard-accessible).


SVG 2 now incorporates keyboard navigation based on the established model from HTML 5. The [user agent](https://infra.spec.whatwg.org/#user-agent) provides sequential focus navigation to
SVG elements that are interactive by default (links), or that the author has indicated may receive focus (through the use of
`tabindex` attribute). Focus may also be set or removed programmatically by scripts, so that authors may implement more complex keyboard focus patterns.


SVG closely aligns with the core DOM Standard \[[DOM](https://www.w3.org/TR/svg-aam-1.0/#bib-dom "DOM Standard")\], supporting JavaScript manipulation of the graphic in interactive environments. Through the use of JavaScript,
CSS, and related APIs, authors can make SVG look and behave as an interactive application, to produce rich interactive charts and drawings.


To allow the author to express and dynamically update their intended semantics in both static and interactive graphics, SVG 2 supports the use of
WAI-ARIA roles, states, and properties. Authors may include
WAI-ARIA attributes in their markup and user agents will translate it to the platform accessibility
APIs.


WAI-ARIA enables rich SVG-drawn Internet applications to have the same accessibility features as
GUI applications installed on their operating system. In complex static graphics, WAI-ARIA provides the missing document structure that is
provided in HTML by semantic elements.


### 1.2 Relationship to Other Specifications

[Permalink for Section 1.2](https://www.w3.org/TR/svg-aam-1.0/#intro_wai-aria_suite)

For an introduction to WAI-ARIA, see the
[WAI-ARIA Overview](https://www.w3.org/WAI/intro/aria.php).


The SVG Accessibility API Mappings specification (this document) defines how WAI-ARIA features interact with the native semantics
of the SVG language. It is part of a set of resources that define and support the WAI-ARIA specification, including the following
documents:


- [Accessible Rich Internet Applications (WAI-ARIA) 1.1](https://www.w3.org/TR/wai-aria-1.1/) \[[WAI-ARIA](https://www.w3.org/TR/svg-aam-1.0/#bib-wai-aria "Accessible Rich Internet Applications (WAI-ARIA) 1.1")\], a planned
   W3C recommendation that extends the existing ARIA standard \[[WAI-ARIA-10](https://www.w3.org/TR/svg-aam-1.0/#bib-wai-aria-10 "Accessible Rich Internet Applications (WAI-ARIA) 1.0")\]. It defines the core roles, states, and properties.

- [WAI-ARIA Graphics Module](https://www.w3.org/TR/graphics-aria-1.0/) \[[GRAPHICS-ARIA](https://www.w3.org/TR/svg-aam-1.0/#bib-graphics-aria "WAI-ARIA Graphics Module")\], a planned W3C recommendation
   that defines graphics roles, states, and properties not included in
   [Accessible Rich Internet Applications (WAI-ARIA) 1.1](https://www.w3.org/TR/wai-aria-1.1/) \[[WAI-ARIA](https://www.w3.org/TR/svg-aam-1.0/#bib-wai-aria "Accessible Rich Internet Applications (WAI-ARIA) 1.1")\].

- [Core Accessibility API Mappings](https://www.w3.org/TR/core-aam-1.1/) specification \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\], which expresses how
   WAI-ARIA [roles](https://www.w3.org/TR/wai-aria-1.3/#dfn-role), [states](https://www.w3.org/TR/wai-aria-1.3/#dfn-state), and
   [properties](https://www.w3.org/TR/wai-aria-1.3/#dfn-property) should be supported in user agents using platform accessibility APIs.

- [Graphics Accessibility API Mappings](https://www.w3.org/TR/graphics-aam-1.0/)\[[GRAPHICS-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-graphics-aam "Graphics Accessibility API Mappings")\], a planned W3C recommendation, which expresses how
   [WAI-ARIA Graphics Module](https://www.w3.org/TR/graphics-aria-1.0/) \[[GRAPHICS-ARIA](https://www.w3.org/TR/svg-aam-1.0/#bib-graphics-aria "WAI-ARIA Graphics Module")\] [roles](https://www.w3.org/TR/wai-aria-1.3/#dfn-role),
   [states](https://www.w3.org/TR/wai-aria-1.3/#dfn-state), and [properties](https://www.w3.org/TR/wai-aria-1.3/#dfn-property) should be supported in user agents using platform accessibility
   APIs.

- [Accessible Name and Description: Computation and API Mappings 1.1](https://www.w3.org/TR/accname-1.1/) \[[ACCNAME-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-accname-aam "Accessible Name and Description Computation 1.1")\], which outlines the specific steps user
   agents should follow in order to identify accessible names (labels) and descriptions (alternative text) for elements that are exposed to assistive technologies.

- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/), a WAI resource that describes how web content developers can develop accessible rich internet applications using WAI-ARIA. It
   provides detailed advice and examples directed primarily to web application developers, yet also useful to developers of user agents and assistive technologies.


This guide relies heavily on the accessibility API mappings defined in the
[Core Accessibility API Mappings](https://www.w3.org/TR/core-aam-1.1/)
and
[Accessible Name and Description](https://www.w3.org/TR/accname-1.2/)
specifications (\[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\] and \[[ACCNAME-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-accname-aam "Accessible Name and Description Computation 1.1")\]) but defines changes in mappings due to features in the SVG host language \[[SVG2](https://www.w3.org/TR/svg-aam-1.0/#bib-svg2 "Scalable Vector Graphics (SVG) 2")\]. Key areas of difference stem from the intrinsic host
language semantics of SVG:


- The procedure for mapping the DOM tree to the accessibility tree is designed to simplify that tree to only include elements with semantic importance.
- SVG elements are assigned default roles and properties, which in many cases are conditional on whether they meet the criteria for inclusion in the accessibility tree.
- Text computation of names and descriptions use the SVG metadata elements.
- Implicit ARIA states (such as whether an element is hidden) must be updated in response to SVG animations.

### 1.3 Accessibility APIs

[Permalink for Section 1.3](https://www.w3.org/TR/svg-aam-1.0/#intro_aapi)

To provide access to GUI applications, software applications expose the necessary information needed by
[assistive technologies](https://www.w3.org/TR/wai-aria-1.3/#dfn-assistive-technologies) to interoperate with it through
[accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api). The accessibility information exposed through the
[accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) must be maintained throughout the applications lifecycle.


In Web pages the Document Object Model (DOM) is used to represent the structure and [state](https://www.w3.org/TR/wai-aria-1.3/#dfn-state) of the [elements](https://dom.spec.whatwg.org/#concept-element) in
the document being rendered by a [user agent](https://infra.spec.whatwg.org/#user-agent). The elements of the document are organized into a hierarchy of nodes known as the
DOM tree. User agents map DOM to accessibility
APIs, in the same way desktop applications map UI components. The information provided to the accessibility API is used to support
assistive technologies, with the expectation that the information passed from the DOM matches the semantic intent of the author. The author may communicate this semantic intent by using
native features of the document language or by using WAI-ARIA, if native features are not available.


Authors use SVG to create a broad range of applications and drawings. The information needed to support accessibility APIs in
SVG comes from a combination of semantics from the elements themselves but also the additional semantics provided by
WAI-ARIA and the modular extensions to WAI-ARIA supported by this
specification.


A screen reader or other assistive technology uses the semantic information exposed via the accessibility API
to provide an alternative rendering of an application that is meaningful to a user.


Accessibility APIs
supported by this document (and the other specifications it extends) are:


- [Microsoft Active Accessibility 2.0](https://msdn.microsoft.com/en-us/library/ms697707.aspx) \[[MSAA](https://www.w3.org/TR/svg-aam-1.0/#bib-msaa "Microsoft Active Accessibility (MSAA)")\] with
   [IAccessible2 1.3](https://wiki.linuxfoundation.org/accessibility/iaccessible2/start) \[[IAccessible2](https://www.w3.org/TR/svg-aam-1.0/#bib-iaccessible2 "IAccessible2")\]

- [User Interface Automation](https://msdn.microsoft.com/en-us/library/ee684013%28VS.85%29.aspx) \[[UI-AUTOMATION](https://www.w3.org/TR/svg-aam-1.0/#bib-ui-automation "UI Automation")\]

- [Linux Accessibility Toolkit 2.10.0](https://developer.gnome.org/atk/2.10/) \[[ATK](https://www.w3.org/TR/svg-aam-1.0/#bib-atk "ATK - Accessibility Toolkit")\] and
   [Assistive Technology - Service Provider Interface 2.1](https://gitlab.gnome.org/GNOME/at-spi2-core/) \[[AT-SPI](https://www.w3.org/TR/svg-aam-1.0/#bib-at-spi "Assistive Technology Service Provider Interface")\]

- [Mac OS X Accessibility Protocol Mac OS 10.10](https://developer.apple.com/documentation/appkit/accessibility/nsaccessibility) \[[AXAPI](https://www.w3.org/TR/svg-aam-1.0/#bib-axapi "The NSAccessibility Protocol for macOS")\]


If user agent developers need to expose information using other accessibility APIs, it is recommended that they work closely with the
developer of the platform where the API runs, and assistive technology developers on that platform.


### 1.4 The Accessibility Tree and the DOM Tree

[Permalink for Section 1.4](https://www.w3.org/TR/svg-aam-1.0/#intro_treetypes)

The [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree) and the DOM tree are parallel structures. Roughly speaking, the
accessibility tree is a subset of the flattened DOM tree, which is then augmented to include the user interface
[objects](https://www.w3.org/TR/wai-aria-1.3/#dfn-object) of the [user agent](https://infra.spec.whatwg.org/#user-agent)
as well as the objects of the document.


[Accessible objects](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) are created in the accessibility tree for every DOM [element](https://dom.spec.whatwg.org/#concept-element)
that should be exposed to an
[assistive technology](https://www.w3.org/TR/wai-aria-1.3/#dfn-assistive-technologies). An element could be exposed because it may fire an accessibility
[event](https://dom.spec.whatwg.org/#concept-event) or because it has a [property](https://www.w3.org/TR/wai-aria-1.3/#dfn-property), relationship or feature which needs to be exposed.


Generally, if a DOM element can be omitted from the accessibility tree without affecting meaning, it will be, for reasons of performance and simplicity. For example, a
`<span>` with just a style change and no [semantics](https://www.w3.org/TR/wai-aria/#dfn-semantics)
may not get its own accessible object, but the style change will be exposed by other means.


## 2\. Conformance

[Permalink for Section 2.](https://www.w3.org/TR/svg-aam-1.0/#conformance)

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words _MAY_, _MUST_, _MUST NOT_, _OPTIONAL_, _RECOMMENDED_, _REQUIRED_, _SHALL_, _SHALL NOT_, _SHOULD_, and _SHOULD NOT_ in this document
are to be interpreted as described in
[BCP 14](https://www.rfc-editor.org/info/bcp14)
\[[RFC2119](https://www.w3.org/TR/svg-aam-1.0/#bib-rfc2119 "Key words for use in RFCs to Indicate Requirement Levels")\] \[[RFC8174](https://www.w3.org/TR/svg-aam-1.0/#bib-rfc8174 "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words")\]
when, and only when, they appear in all
capitals, as shown here.


### 2.1 Normative User Agent Implementation Requirements for SVG

[Permalink for Section 2.1](https://www.w3.org/TR/svg-aam-1.0/#normative-user-agent-implementation-requirements-for-svg)

This specification marks certain sections as non-normative, also called informative. The classification applies to the entire section. All other sections provide normative requirements. A
statement "This section is non-normative" applies to all its sub-sections, unless otherwise indicated. In addition, all text boxes labelled "Note" are informative.


Normative sections provide requirements that [user agents](https://infra.spec.whatwg.org/#user-agent) must follow for an implementation to conform to this specification. The keywords _MUST_, _MUST NOT_, _REQUIRED_, _SHALL_, _SHALL NOT_,
_SHOULD_, _RECOMMENDED_, _MAY_, and _OPTIONAL_ in this document are to be interpreted as described in
[Keywords for use in RFCs to indicate requirement levels](http://www.rfc-editor.org/rfc/rfc2119.txt) \[[rfc2119](https://www.w3.org/TR/svg-aam-1.0/#bib-rfc2119 "Key words for use in RFCs to Indicate Requirement Levels")\]. RFC-2119 keywords are formatted in uppercase and
contained in an element with `class="rfc2119"`. When the keywords shown above are used, but do not share this format, they do not convey formal information in the RFC 2119 sense,
and are merely explanatory, i.e., informative. As much as possible, such usages are avoided in this specification.


Informative sections and notes provide information useful to understanding the specification. Such sections may contain examples of recommended practice, but it is not required to follow such
recommendations in order to conform to this specification.


## 3\. Supporting Keyboard Navigation

[Permalink for Section 3.](https://www.w3.org/TR/svg-aam-1.0/#keyboard-focus)

Enabling keyboard navigation in web applications is a necessary step toward making accessible web applications possible. Not only is the keyboard the primary input device for many users, but
other accessible input devices use keyboard events to communicate with the user agent.


The Scalable Vector Graphics (SVG) 1 \[[SVG1](https://www.w3.org/TR/svg-aam-1.0/#bib-svg1 "Scalable Vector Graphics (SVG) 1.0 Specification")\] and 1.1 \[[SVG11](https://www.w3.org/TR/svg-aam-1.0/#bib-svg11 "Scalable Vector Graphics (SVG) 1.1 (Second Edition)")\] specifications included only very limited keyboard support (access keys for animations). Many user agents implemented tabbed
focus for links, but there was no declarative or scripted means for authors to control this behavior. Scalable Vector Graphics (SVG) 2 \[[SVG2](https://www.w3.org/TR/svg-aam-1.0/#bib-svg2 "Scalable Vector Graphics (SVG) 2")\] introduces keyboard navigation and focus control
based on the HTML `tabindex` model.


Conforming user agents _MUST_ conform to
[Supporting Keyboard Navigation](https://www.w3.org/TR/core-aam-1.1/#keyboard-focus)
requirements in the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


Note

The SVG Accessibility Task Force intends to develop more detailed guidelines for authors and user agents regarding navigation in graphical documents.

## 4\. Mapping WAI-ARIA to Accessibility APIs

[Permalink for Section 4.](https://www.w3.org/TR/svg-aam-1.0/#mapping)

WAI-ARIA support was formally introduced to SVG in Scalable Vector Graphics (SVG) 2 \[[SVG2](https://www.w3.org/TR/svg-aam-1.0/#bib-svg2 "Scalable Vector Graphics (SVG) 2")\], which allows ARIA attributes to be used
in the default namespace. This section defines how WAI-ARIA semantics are exposed to assistive technologies through platform Accessibility
APIs and how SVG elements are mapped to Accessibility APIs based on WAI-ARIA.


### 4.1 General rules for exposing WAI-ARIA semantics

[Permalink for Section 4.1](https://www.w3.org/TR/svg-aam-1.0/#mapping_general)

SVG user agents **_MUST_** conform to [General rules for exposing WAI-ARIA semantics](https://www.w3.org/TR/core-aam-1.1/#mapping_general) in the Core Accessibility
API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\], with the additions described in the following sub-sections.


#### 4.1.1 Excluding Elements from the Accessibility Tree

[Permalink for Section 4.1.1](https://www.w3.org/TR/svg-aam-1.0/#exclude_elements)

Certain elements in the DOM are not exposed via the
[accessibility API](https://www.w3.org/TR/wai-aria-1.3/#dfn-accessibility-api). The section [Excluding Elements from the Accessibility Tree](https://www.w3.org/TR/core-aam-1.1/#exclude_elements2)
of the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\] outlines the general rules for excluding elements. One factor is whether host language semantics specify that the element should not be
displayed.


The SVG language defines numerous elements that fit this criteria. Many SVG elements are never directly rendered to the screen, while others may or may not be rendered or displayed,
depending on context or CSS styling. Elements which are neither perceivable nor interactive should not be included in the accessibility tree exposed to accessibility
APIs. This section details the expected interpretation of SVG host language semantics.


Note

The other factors for excluding elements, as described in the Core Accessibility API Mappings, can be summarized as follows:

- If the first mappable role provided by the author is [`none`](https://www.w3.org/TR/wai-aria-1.3/) or
[`presentation`](https://www.w3.org/TR/wai-aria-1.3/#presentation), the element must not be exposed.

- If the element or an ancestor has an [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.3/#aria-hidden) value of `true`, it should not be exposed.

- If an ancestor of the element has a used role which has the characteristic " [Children Presentational: True](https://www.w3.org/TR/wai-aria-1.3/#childrenArePresentational)" in the
WAI-ARIA specifications \[[WAI-ARIA](https://www.w3.org/TR/svg-aam-1.0/#bib-wai-aria "Accessible Rich Internet Applications (WAI-ARIA) 1.1")\], the child element should not be exposed. For example, the roles [`button`](https://www.w3.org/TR/wai-aria-1.3/#button) and
[`img`](https://www.w3.org/TR/wai-aria-1.3/#img)
exclude all child content from being directly included in the accessibility tree.


However, note that a number of features of an element, such as interactivity, can cause
[an author-supplied or inherited role of `none` or `presentation` to be ignored as an error.](https://www.w3.org/TR/wai-aria-1.3/#conflict_resolution_presentation_none)
An element will not be excluded if it can currently receive focus based on user interaction.


Consult the [original document](https://www.w3.org/TR/core-aam-1.1/#exclude_elements2) (\[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\]) for the normative text.

Elements which are never directly rendered to screen, nor represented by an interactive region in a graphic, do not need a corresponding accessible object. User agents
**_MUST NOT_** include any elements, or their descendant content, as an [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) in the
[accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree) that are indicated as `no accessible object created` in the
[SVG Element Mapping Tables](https://www.w3.org/TR/svg-aam-1.0/#mapping_role_table). User agents **_SHOULD_** also exclude any other element defined by past or future SVG
specifications or modules that specifically indicate the element is [never directly rendered](https://www.w3.org/TR/SVG2/render.html#TermNeverRenderedElement).


For example, elements that represent filters, gradients, or gradient stops will never create an accessible object. Shape elements or image elements that are included in an SVG definitions
section or as part of a pattern will also not have accessible objects, because the semantics of the ancestor
`defs` or `pattern` element preclude that entire DOM subtree from being represented in the accessibility tree.


Elements that are excluded from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree) might still be used in the name and description computation of another element,
as defined in the [Name and Description](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional_nd) section. Non-rendered elements may also be used as the templates for rendered element instances created by a
`use` element, as described in the section on [Use-Element Shadow Trees](https://www.w3.org/TR/svg-aam-1.0/#mapping_use_shadow_tree).


Note

Although they are not directly included in the accessibility tree, animation and view elements can affect the accessible objects representing their target elements, as described under
[Special Processing Requiring Additional Computation](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional).


In addition, SVG 1.1 \[[SVG11](https://www.w3.org/TR/svg-aam-1.0/#bib-svg11 "Scalable Vector Graphics (SVG) 1.1 (Second Edition)")\] defines the conditional processing attributes
`systemLanguage`, `requiredExtensions`, and `requiredFeatures`. These may be used individually or in combination with the `switch` element to
prevent content from being rendered under certain conditions, or to select between alternate versions of content.


SVG user agents **_MUST NOT_** expose to accessibility APIs any elements that are not rendered because of conditional processing attributes on that element or
because of the position of that element within a switch construct. The `switch` element itself **_SHOULD_** be omitted as if it had a role of
`none` or `presentation`.


The rendering of SVG elements is also affected by CSS styling properties, which may be specified using stylesheet rules, inline styles, presentation attributes, or animations. Regardless
of how the style property is specified, the effect depends on the final computed value determined by the CSS cascade \[[CSS-CASCADE-3](https://www.w3.org/TR/svg-aam-1.0/#bib-css-cascade-3 "CSS Cascading and Inheritance Level 3")\]. User agents
**_MUST NOT_** expose to accessibility APIs any element that is not rendered because its computed style includes a value of `none` for the
[`display`](https://svgwg.org/svg2-draft/render.html#VisibilityControl) property.


Other style properties can prevent an element, which is otherwise part of the rendering tree, from creating any visible representation in the rendered graphic. Such elements may still be
interactive; they may receive keyboard focus or they may be associated with a region of the graphic that is responsive to pointer input events.


For the purpose of SVG, an element is considered [hidden](https://www.w3.org/TR/wai-aria-1.3/#dfn-hidden) if it is _neither_ visible, according to the computed value of the
[`visibility`](https://svgwg.org/svg2-draft/render.html#VisibilityControl) property, nor interactive to pointer users. according to the
[`pointer-events`](https://svgwg.org/svg2-draft/interact.html#PointerEventsProperty) property. User agents **_SHOULD NOT_**
expose to accessibility APIs any element that is hidden in this sense,
_unless_ the author explicitly overrides the hiding by setting the [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.3/#aria-hidden) attribute to `false`.


In the case of container elements (such as `g` or `svg`), the element is not considered hidden if _any_ of its descendent content is visible _or_ can
receive user events, regardless of the computed value of `visibility` on the element itself. Similarly, a `use` element may include visible or interactive component
graphics, despite having style properties that would cause an individual shape element to be hidden. The `use` element _MUST_ be considered visible or interactive if any elements
within its shadow tree are visible or interactive. (The container or the `use` element may, however, still be considered presentational if it does not have any other reason to
include it in the accessibility tree.) A shape element with markers is visible or interactive if any of its markers are visible or interactive.


Note

In HTML and in other CSS-styled documents, elements made invisible with `visibility: hidden` are always hidden elements for accessibility purposes, equivalent to un-rendered
elements (such as those with `display: none`).


For SVG, this is not always appropriate, because of the interaction with the `pointer-events` property.

In many cases, the invisible elements are of semantic importance (because they are interactive) while visible elements are presentational only. For example, large invisible elements are
often used to provide easy-to-hit targets for points in a map or datachart. Because these elements react to pointer events, they are effectively perceivable to pointer users, and should
be perceivable and interactive to users of assistive technologies as well.


An SVG element with a computed value of `visibility: hidden`
can be interactive to pointer users for the following values of the
[`pointer-events`](https://svgwg.org/svg2-draft/interact.html#PointerEventsProperty) property:


- `painted`, for any rendered element _except_ shape or a text where both the `fill` and `stroke` properties have a computed value of
`none`
- `fill`
- `stroke`
- `all`
- `bounding-box`

An element that is currently positioned off-screen, or that is obscured by other elements, is not considered hidden. User agents should expose this state through other means, as described
in the [State and Property Mapping](https://www.w3.org/TR/core-aam-1.1/#statePropertyMappingGeneralRules)
section of the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


Note

Various other style properties and geometric attributes (of an element itself or an ancestor element) can make an element invisible. For simplicity, flexibility, and performance reasons,
these are not considered a hiding method that excludes elements from the accessibility tree.


When using properties other than `display` or `visibility` to hide inactive content, authors can use the
[`aria-hidden`](https://www.w3.org/TR/wai-aria-1.3/#aria-hidden) attribute to indicate that assistive technologies should ignore the element and its descendants.


Editor's note

Previous drafts of this specification also considered the
`fill` and `stroke` properties, when both set to a value of `none`, as a valid way to hide an element. This has been removed as it introduced excessive
complexity. Some SVG elements (e.g., embedded images) are not affected by stroke and fill; even those that are can be visible without it, because of markers or filter effects.
Furthermore, it could result in identical-looking graphics (for example: one that used `fill: transparent` instead of `fill: none`) having markedly different
accessibility trees.


Note, however, that the `fill` and `stroke` properties may still have an indirect effect on the inclusion of an element, depending on the value of the
`pointer-events` property.


[Issue 6](https://github.com/w3c/svg-aam/issues/6): Should structured descriptions be exposed in the accessibility tree? [Needs ARIA WG Input](https://github.com/w3c/svg-aam/issues/?q=is%3Aissue+is%3Aopen+label%3A%22Needs+ARIA+WG+Input%22) [Needs Implementer Input](https://github.com/w3c/svg-aam/issues/?q=is%3Aissue+is%3Aopen+label%3A%22Needs+Implementer+Input%22)

The strict exclusion of non-rendered metadata elements, including `desc`, from the accessibility tree means that their content will only be available as plain text, not as
structured alternative representations that a user can navigate in browsing mode.


This contradicts the original intent of the SVG specifications, which allows these elements to include structured content, including HTML-namespaced content. The SVG 1 specifications had
suggested that this could be alternatively presented as CSS-formatted XML text, but this is not supported by the user agent/assistive technology combinations currently in use.


The editors welcome feedback and suggestions (in [GitHub Issue #6](https://github.com/w3c/svg-aam/issues/6)) on alternative ways to represent this hidden alternative content
in a way consistent with user agent and accessibility API implementations.


#### 4.1.2 Including Elements in the Accessibility Tree

[Permalink for Section 4.1.2](https://www.w3.org/TR/svg-aam-1.0/#include_elements)

Many SVG elements—although rendered to the screen—do not have an intrinsic semantic meaning. Instead, they represent components of the visual presentation of the document. To
simplify the accessible representation of the document, these purely presentational elements should normally be omitted from the accessibility tree, unless the author explicitly provides
semantic content.


However, any rendered SVG element may have semantic meaning. Authors indicate the significance of the element by including alternative text content or
WAI-ARIA attributes. This section defines the rules for including normally-omitted elements in the accessibility tree.


The following graphical and container elements in the SVG namespace
**_SHOULD NOT_** be included in the accessibility tree, _except_ as described in this section:


- shape elements (`circle`,
   `ellipse`, `line`, `path`, `polygon`, `polyline`, `rect`)

- the `use` element
- the grouping (`g`) element
- the `image` element
- text formatting elements (`textPath`,
   `tspan`)

- the `foreignObject` element

Although these elements are omitted from the accessibility tree, their child content is still processed, as if it was a direct child of the nearest ancestor node in the DOM tree that is
included in the accessibility tree. In other words, the markup elements are treated as if they had a role of `none` or `presentation`.


For `use` elements, the elements and text in their associated shadow tree _MUST_ be processed as if it was child content of the `use` element, following the conditions
specified in [processing requiring additional computation](https://www.w3.org/TR/svg-aam-1.0/#mapping_use_shadow_tree). This means that elements from the shadow tree can be included in the accessibility tree
even if the `use` element itself has a (default or author-supplied) role of `presentation`.


SVG user agents **_MUST_** provide an accessible object in the accessibility tree for rendered SVG elements that meet any of the following criteria,
_unless_ they are excluded from the accessibility tree per the rules in [Excluding Elements from the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#exclude_elements):


- It has at least one direct child
   ‘ [title](https://www.w3.org/TR/SVG2/struct.html#TitleElement)’
   element or
   ‘ [desc](https://www.w3.org/TR/SVG2/struct.html#DescElement)'
   element that is not empty after trimming whitespace. User agents _MAY_ include elements with these child elements without checking for valid text content.

- It has a non-empty (after trimming whitespace)
   ‘ [aria-label](https://www.w3.org/TR/wai-aria-1.3/#aria-label)’
   attribute or
   ‘ [aria-roledescription](https://www.w3.org/TR/wai-aria-1.3/#aria-roledescription)’
   attribute.

- It has an
   ‘ [aria-labelledby](https://www.w3.org/TR/wai-aria-1.3/#aria-labelledby)’
   attribute or
   ‘ [aria-describedby](https://www.w3.org/TR/wai-aria-1.3/#aria-describedby)’
   attribute containing valid IDREF tokens. User agents _MAY_ include elements with these attributes without checking for validity.

- It has a valid integer
   ' [tabindex](https://www.w3.org/TR/SVG2/struct.html#SVGElementTabindexAttribute)'
   attribute.

- The author has provided an allowed, non-abstract
   WAI-ARIA role other than `none` or
   `presentation`.

- It meets any of the criteria listed in the section
   [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements)
   of the Core Accessibility API Mappings specification \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


Note

At the time of drafting this document, those criteria are as follows:



- Text elements
- Elements that may fire an accessibility API [event](https://dom.spec.whatwg.org/#concept-event)
- Elements that are focusable, or have an ID [attribute](https://dom.spec.whatwg.org/#concept-attribute) and an ancestor with the
[`aria-activedescendant`](https://www.w3.org/TR/wai-aria-1.3/#aria-activedescendant) attribute that matches the implicit or explicit [semantics](https://www.w3.org/TR/wai-aria/#dfn-semantics) of
the required context role. In either case, the element may receive focus and need to fire a` FOCUS`event.

- Elements that have a mappable role in the role attribute string (see [Role Mapping](https://www.w3.org/TR/core-aam-1.1/#mapping_role)).
- Elements that have a global WAI-ARIA attribute  but do not have
[`aria-hidden`](https://www.w3.org/TR/wai-aria-1.3/#aria-hidden)`="true"`. (See [Excluding Elements in the Accessibility Tree](https://www.w3.org/TR/core-aam-1.1/#exclude_elements2) for additional guidance on
`aria-hidden`.)

- Elements that have an ID which is referenced by another element via a WAI-ARIA relation ( [`aria-controls`](https://www.w3.org/TR/wai-aria-1.3/), [`aria-describedby`](https://www.w3.org/TR/wai-aria-1.3/#aria-describedby), [`aria-flowto`](https://www.w3.org/TR/wai-aria-1.3/#aria-flowto), [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.3/#aria-labelledby) or [`aria-owns`](https://www.w3.org/TR/wai-aria-1.3/#aria-labelledby)) and are not [hidden](https://www.w3.org/TR/wai-aria-1.3/#dfn-hidden).


The latest version of the source document \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\] should be consulted for the normative text.

The exception for hidden elements means that SVG metadata elements or other non-rendered content may be used in the accessible name and description of another element without themselves
being included in the accessibility tree. For example, current best practice for fallback browser support is to use `aria-labelledby` and `aria-describedby`
to redundantly link to
`title` and `desc` child elements. Including these elements as separate nodes in the tree would unnecessarily complicate the document presented to screen reader
users.


Interactive elements are covered by the requirement regarding elements that may fire an Accessibility API event. Specifically, for SVG the following elements are interactive and _MUST_ be
included in the accessibility tree, without exception, regardless of whether they would otherwise be considered hidden or presentational:


- A [rendered](https://svgwg.org/svg2-draft/render.html#TermRenderedElement) element (or instance of an element in a use-element shadow tree) with a positive integer value for
   the `tabindex` attribute, or which is [focusable](https://svgwg.org/svg2-draft/interact.html#TermFocusable) by default and has not been removed from the tab order
   with a negative integer `tabindex` attribute, which may receive keyboard focus and therefore keyboard input events.

- A [rendered](https://svgwg.org/svg2-draft/render.html#TermRenderedElement) element (or instance of an element) that currently has keyboard
   [focus](https://svgwg.org/svg2-draft/interact.html#Focus)
   (e.g., after being focused from a script), which may receive keyboard input events.


With regards to pointer events, which bubble up the DOM tree, the exact element that receives the event may not have semantic meaning (that is, it may still be presentational). However,
the ability to receive pointer events overrides any exclusion based on the `visibility: hidden` style property.


Note

The `tabindex` attribute and the `pointer-events` property have no impact on elements which are not rendered at all, because of the
`display: none` property or because of host language semantics.


### 4.2 Conflicts between native markup semantics and WAI-ARIA

[Permalink for Section 4.2](https://www.w3.org/TR/svg-aam-1.0/#mapping_conflicts)

SVG user agents _MUST_ conform to
[Conflicts between native markup semantics and WAI-ARIA](https://www.w3.org/TR/core-aam-1.1/#mapping_conflicts) in the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\] where the host language is
SVG and the native semantics are as described in the [SVG Element Mapping Tables](https://www.w3.org/TR/svg-aam-1.0/#mapping_role_table), the
[State and Property Mapping](https://www.w3.org/TR/svg-aam-1.0/#mapping_state-property) section, and the [Special Processing Requiring Additional Computation](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional) section.


Elements for which no accessible object is created and no role may be applied, as defined in the [SVG Element Mapping Tables](https://www.w3.org/TR/svg-aam-1.0/#mapping_role_table), have no implicit role
[semantics](https://www.w3.org/TR/wai-aria-1.3/#dfn-semantics). The
‘ [aria-roledescription](https://www.w3.org/TR/wai-aria-1.3/#aria-roledescription)’
attribute _MUST NOT_ be exposed on these elements. All other SVG elements have implicit role semantics when used with global WAI-ARIA attributes, including
‘ [aria-roledescription](https://www.w3.org/TR/wai-aria-1.3/#aria-roledescription)’.


### 4.3 Exposing attributes that do not directly map to accessibility API properties

[Permalink for Section 4.3](https://www.w3.org/TR/svg-aam-1.0/#mapping_nodirect)

SVG user agents _MUST_ conform to
[Exposing attributes that do not directly map to accessibility API properties](https://www.w3.org/TR/core-aam-1.1/#mapping_nodirect) in
the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


## 5\. Role mapping

[Permalink for Section 5.](https://www.w3.org/TR/svg-aam-1.0/#mapping_role)

Platform [accessibility APIs](https://www.w3.org/TR/wai-aria-1.3/#dfn-accessibility-api) traditionally have had a finite set of predefined
[roles](https://www.w3.org/TR/wai-aria-1.3/#dfn-role) that are expected by [assistive technologies](https://www.w3.org/TR/wai-aria-1.3/#dfn-assistive-technologies)
on that platform and only one or two roles may be exposed.


WAI-ARIA
only supports one active role at a time. However, multiple roles may be specified as an ordered set of space-separated valid role tokens. The additional roles are fallback roles, similar to
the concept of specifying multiple font families in case the first choice font is not supported. This allows the role taxonomy to be extended in future for specialized applications. The entire
role string is exposed to accessibility technologies where possible, so they can respond appropriately even if there is no equivalent role in the platform
API.


### 5.1 General Rules

[Permalink for Section 5.1](https://www.w3.org/TR/svg-aam-1.0/#roleMappingGeneralRules)

SVG user agents _MUST_ conform to the Role Mapping [General Rules](https://www.w3.org/TR/core-aam-1.1/#mapping_general) accessibility API computational requirements
in the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


### 5.2 SVG Element Mapping Tables

[Permalink for Section 5.2](https://www.w3.org/TR/svg-aam-1.0/#mapping_role_table)

This section defines how elements in SVG2 map to WAI-ARIA roles and platform accessibility APIs based on their native host language semantics, including which WAI-ARIA roles may be applied.
This section refers directly to both the
[`Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table)
in the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\] specification and the [`Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) in the Graphics Accessibility
API Mappings \[[GRAPHICS-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-graphics-aam "Graphics Accessibility API Mappings")\] specification, which define how WAI-ARIA roles are mapped to platform accessibility APIs.


#### 5.2.1 `a`

[Permalink for Section 5.2.1](https://www.w3.org/TR/svg-aam-1.0/#role-map-a)

| SVG Specification | [`a`](https://www.w3.org/TR/SVG2/linking.html#AElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`link`](https://www.w3.org/TR/core-aam-1.1/#role-map-link) role if the element has a valid `href` or `xlink:href` attribute. For `a` elements<br> that are not links, use the mapping for `tspan` if the `a` element is a descendent of `text`, or the mapping for `g` otherwise. |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.2 `animate`

[Permalink for Section 5.2.2](https://www.w3.org/TR/svg-aam-1.0/#role-map-animate)

| SVG Specification | [`animate`](https://svgwg.org/specs/animations/#AnimateElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.3 `animateMotion`

[Permalink for Section 5.2.3](https://www.w3.org/TR/svg-aam-1.0/#role-map-animatemotion)

| SVG Specification | [`animateMotion`](https://svgwg.org/specs/animations/#AnimateMotionElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.4 `animateTransform`

[Permalink for Section 5.2.4](https://www.w3.org/TR/svg-aam-1.0/#role-map-animatetransform)

| SVG Specification | [`animateTransform`](https://svgwg.org/specs/animations/#AnimateTransformElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.5 `circle`

[Permalink for Section 5.2.5](https://www.w3.org/TR/svg-aam-1.0/#role-map-circle)

| SVG Specification | [`circle`](https://www.w3.org/TR/SVG2/shapes.html#CircleElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`graphics-symbol`](https://www.w3.org/TR/graphics-aam-1.0/#role-map-graphics-symbol) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.6 `clipPath`

[Permalink for Section 5.2.6](https://www.w3.org/TR/svg-aam-1.0/#role-clippath)

| SVG Specification | [`clipPath`](https://www.w3.org/TR/2012/WD-css-masking-20121115/#ClipPathElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created, for this element or any child content |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.7 `defs`

[Permalink for Section 5.2.7](https://www.w3.org/TR/svg-aam-1.0/#role-map-defs)

| SVG Specification | [`defs`](https://www.w3.org/TR/SVG2/struct.html#DefsElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created, for this element or any child content |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.8 `desc`

[Permalink for Section 5.2.8](https://www.w3.org/TR/svg-aam-1.0/#role-map-desc)

| SVG Specification | [`desc`](https://www.w3.org/TR/SVG2/struct.html#DescElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created, for this element or any child content; see<br> [Name and Description](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional_nd) mapping |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.9 `ellipse`

[Permalink for Section 5.2.9](https://www.w3.org/TR/svg-aam-1.0/#role-map-ellipse)

| SVG Specification | [`ellipse`](https://www.w3.org/TR/SVG2/shapes.html#EllipseElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`graphics-symbol`](https://www.w3.org/TR/graphics-aam-1.0/#role-map-graphics-symbol) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.10 `feBlend`

[Permalink for Section 5.2.10](https://www.w3.org/TR/svg-aam-1.0/#role-map-feblend)

| SVG Specification | [`feBlend`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feBlendElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.11 `feColorMatrix`

[Permalink for Section 5.2.11](https://www.w3.org/TR/svg-aam-1.0/#role-map-feColorMatrix)

| SVG Specification | [`feColorMatrix`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feColorMatrixElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.12 `feComponentTransfer`

[Permalink for Section 5.2.12](https://www.w3.org/TR/svg-aam-1.0/#role-map-feComponentTransfer)

| SVG Specification | [`feComponentTransfer`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feComponentTransferElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.13 `feComposite`

[Permalink for Section 5.2.13](https://www.w3.org/TR/svg-aam-1.0/#role-map-feComposite)

| SVG Specification | [`feComposite`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feCompositeElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.14 `feConvolveMatrix`

[Permalink for Section 5.2.14](https://www.w3.org/TR/svg-aam-1.0/#role-map-feConvolveMatrix)

| SVG Specification | [`feConvolveMatrix`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feConvolveMatrixElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.15 `feDiffuseLighting`

[Permalink for Section 5.2.15](https://www.w3.org/TR/svg-aam-1.0/#role-map-fediffuselighting)

| SVG Specification | [`feDiffuseLighting`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feDiffuseLightingElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.16 `feDisplacementMap`

[Permalink for Section 5.2.16](https://www.w3.org/TR/svg-aam-1.0/#role-map-fedisplacementmap)

| SVG Specification | [`feDisplacementMap`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feDisplacementMapElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.17 `feDistantLight`

[Permalink for Section 5.2.17](https://www.w3.org/TR/svg-aam-1.0/#role-map-fedistantlight)

| SVG Specification | [`feDistantLight`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feDistantLightElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.18 `feDropShadow`

[Permalink for Section 5.2.18](https://www.w3.org/TR/svg-aam-1.0/#role-map-fedropshadow)

| SVG Specification | [`feDropShadow`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feDropShadowElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.19 `feFlood`

[Permalink for Section 5.2.19](https://www.w3.org/TR/svg-aam-1.0/#role-map-feflood)

| SVG Specification | [`feFlood`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feFloodElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.20 `feFuncA`

[Permalink for Section 5.2.20](https://www.w3.org/TR/svg-aam-1.0/#role-map-fefunca)

| SVG Specification | [`feFuncA`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feFuncAElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.21 `feFuncB`

[Permalink for Section 5.2.21](https://www.w3.org/TR/svg-aam-1.0/#role-map-fefuncb)

| SVG Specification | [`feFuncB`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feFuncBElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.22 `feFuncG`

[Permalink for Section 5.2.22](https://www.w3.org/TR/svg-aam-1.0/#role-map-fefuncg)

| SVG Specification | [`feFuncG`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feFuncGElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.23 `feFuncR`

[Permalink for Section 5.2.23](https://www.w3.org/TR/svg-aam-1.0/#role-map-fefuncr)

| SVG Specification | [`feFuncR`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feFuncRElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.24 `feGaussianBlur`

[Permalink for Section 5.2.24](https://www.w3.org/TR/svg-aam-1.0/#role-map-fegaussianblur)

| SVG Specification | [`feGaussianBlur`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feGaussianBlurElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.25 `feImage`

[Permalink for Section 5.2.25](https://www.w3.org/TR/svg-aam-1.0/#role-map-feimage)

| SVG Specification | [`feImage`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feImageElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.26 `feMerge`

[Permalink for Section 5.2.26](https://www.w3.org/TR/svg-aam-1.0/#role-map-femerge)

| SVG Specification | [`feMerge`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feMergeElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.27 `feMergeNode`

[Permalink for Section 5.2.27](https://www.w3.org/TR/svg-aam-1.0/#role-map-femergeNode)

| SVG Specification | [`feMergeNode`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#femergenode) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.28 `feMorphology`

[Permalink for Section 5.2.28](https://www.w3.org/TR/svg-aam-1.0/#role-map-femorphology)

| SVG Specification | [`feMorphology`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#femorphology) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.29 `feOffset`

[Permalink for Section 5.2.29](https://www.w3.org/TR/svg-aam-1.0/#role-map-feoffset)

| SVG Specification | [`feOffset`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feoffset) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.30 `fePointLight`

[Permalink for Section 5.2.30](https://www.w3.org/TR/svg-aam-1.0/#role-map-fepointlight)

| SVG Specification | [`fePointLight`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#fePointLightElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.31 `feSpecularLighting`

[Permalink for Section 5.2.31](https://www.w3.org/TR/svg-aam-1.0/#role-map-fespecularlighting)

| SVG Specification | [`feSpecularLighting`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#fespecularlighting) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.32 `feSpotLight`

[Permalink for Section 5.2.32](https://www.w3.org/TR/svg-aam-1.0/#role-map-fespotlight)

| SVG Specification | [`feSpotLight`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feSpotLightElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.33 `feTile`

[Permalink for Section 5.2.33](https://www.w3.org/TR/svg-aam-1.0/#role-map-fetile)

| SVG Specification | [`feTile`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#fetile) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.34 `feTurbulence`

[Permalink for Section 5.2.34](https://www.w3.org/TR/svg-aam-1.0/#role-map-feturbulence)

| SVG Specification | [`feTurbulence`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#feturbulence) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.35 `filter`

[Permalink for Section 5.2.35](https://www.w3.org/TR/svg-aam-1.0/#role-map-filter)

| SVG Specification | [`filter`](https://www.w3.org/TR/2012/WD-filter-effects-20121025/#filter) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.36 `foreignObject`

[Permalink for Section 5.2.36](https://www.w3.org/TR/svg-aam-1.0/#role-map-foreignobject)

| SVG Specification | [`foreignObject`](https://www.w3.org/TR/SVG2/embedded.html#ForeignObjectElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`group`](https://www.w3.org/TR/core-aam-1.1/#role-map-group) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.37 `g`

[Permalink for Section 5.2.37](https://www.w3.org/TR/svg-aam-1.0/#role-map-g)

| SVG Specification | [`g`](https://www.w3.org/TR/SVG2/struct.html#GElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`group`](https://www.w3.org/TR/core-aam-1.1/#role-map-group) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.38 `image`

[Permalink for Section 5.2.38](https://www.w3.org/TR/svg-aam-1.0/#role-map-image)

| SVG Specification | [`image`](https://www.w3.org/TR/SVG2/embedded.html#ImageElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`img`](https://www.w3.org/TR/core-aam-1.1/#role-map-img) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.39 `line`

[Permalink for Section 5.2.39](https://www.w3.org/TR/svg-aam-1.0/#role-map-line)

| SVG Specification | [`line`](https://www.w3.org/TR/SVG2/shapes.html#LineElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`graphics-symbol`](https://www.w3.org/TR/graphics-aam-1.0/#role-map-graphics-symbol) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.40 `linearGradient`

[Permalink for Section 5.2.40](https://www.w3.org/TR/svg-aam-1.0/#role-map-lineargradient)

| SVG Specification | [`linearGradient`](https://www.w3.org/TR/SVG2/pservers.html#LinearGradientElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.41 `marker`

[Permalink for Section 5.2.41](https://www.w3.org/TR/svg-aam-1.0/#role-map-marker)

| SVG Specification | [`marker`](https://www.w3.org/TR/SVG2/painting.html#MarkerElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.42 `mask`

[Permalink for Section 5.2.42](https://www.w3.org/TR/svg-aam-1.0/#role-map-mask)

| SVG Specification | [`mask`](https://www.w3.org/TR/2012/WD-css-masking-20121115/#MaskElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.43 `metadata`

[Permalink for Section 5.2.43](https://www.w3.org/TR/svg-aam-1.0/#role-map-metadata)

| SVG Specification | [`metadata`](https://www.w3.org/TR/SVG2/struct.html#MetadataElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created, for this element or any child content |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.44 `mpath`

[Permalink for Section 5.2.44](https://www.w3.org/TR/svg-aam-1.0/#role-map-mpath)

| SVG Specification | [`mpath`](https://svgwg.org/specs/animations/#MPathElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.45 `path`

[Permalink for Section 5.2.45](https://www.w3.org/TR/svg-aam-1.0/#role-map-path)

| SVG Specification | [`path`](https://www.w3.org/TR/SVG2/paths.html#PathElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`graphics-symbol`](https://www.w3.org/TR/graphics-aam-1.0/#role-map-graphics-symbol) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.46 `pattern`

[Permalink for Section 5.2.46](https://www.w3.org/TR/svg-aam-1.0/#role-map-pattern)

| SVG Specification | [`pattern`](https://www.w3.org/TR/SVG2/pservers.html#PatternElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created, for this element or any child content |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.47 `polygon`

[Permalink for Section 5.2.47](https://www.w3.org/TR/svg-aam-1.0/#role-map-polygon)

| SVG Specification | [`polygon`](https://www.w3.org/TR/SVG2/shapes.html#PolygonElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`graphics-symbol`](https://www.w3.org/TR/graphics-aam-1.0/#role-map-graphics-symbol) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.48 `polyline`

[Permalink for Section 5.2.48](https://www.w3.org/TR/svg-aam-1.0/#role-map-polyline)

| SVG Specification | [`polyline`](https://www.w3.org/TR/SVG2/shapes.html#PolylineElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`graphics-symbol`](https://www.w3.org/TR/graphics-aam-1.0/#role-map-graphics-symbol) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.49 `radialGradient`

[Permalink for Section 5.2.49](https://www.w3.org/TR/svg-aam-1.0/#role-map-radialgradient)

| SVG Specification | [`radialGradient`](https://www.w3.org/TR/SVG2/pservers.html#RadialGradientElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.50 `rect`

[Permalink for Section 5.2.50](https://www.w3.org/TR/svg-aam-1.0/#role-map-rect)

| SVG Specification | [`rect`](https://www.w3.org/TR/SVG2/shapes.html#RectElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`graphics-symbol`](https://www.w3.org/TR/graphics-aam-1.0/#role-map-graphics-symbol) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.51 `script`

[Permalink for Section 5.2.51](https://www.w3.org/TR/svg-aam-1.0/#role-map-script)

| SVG Specification | [`script`](https://www.w3.org/TR/SVG2/interact.html#ScriptElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.52 `set`

[Permalink for Section 5.2.52](https://www.w3.org/TR/svg-aam-1.0/#role-map-set)

| SVG Specification | [`set`](https://svgwg.org/specs/animations/#SetElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.53 `stop`

[Permalink for Section 5.2.53](https://www.w3.org/TR/svg-aam-1.0/#role-map-stop)

| SVG Specification | [`stop`](https://www.w3.org/TR/SVG2/pservers.html#StopElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.54 `style`

[Permalink for Section 5.2.54](https://www.w3.org/TR/svg-aam-1.0/#role-map-style)

| SVG Specification | [`style`](https://www.w3.org/TR/SVG2/styling.html#StyleElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.55 `svg`

[Permalink for Section 5.2.55](https://www.w3.org/TR/svg-aam-1.0/#role-map-svg)

| SVG Specification | [`svg`](https://www.w3.org/TR/SVG2/struct.html#SVGElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`graphics-document`](https://www.w3.org/TR/graphics-aam-1.0/#role-map-graphics-document) |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.56 `switch`

[Permalink for Section 5.2.56](https://www.w3.org/TR/svg-aam-1.0/#role-map-switch)

| SVG Specification | [`switch`](https://www.w3.org/TR/SVG2/struct.html#SwitchElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.57 `symbol`

[Permalink for Section 5.2.57](https://www.w3.org/TR/svg-aam-1.0/#role-map-symbol)

| SVG Specification | [`symbol`](https://www.w3.org/TR/SVG2/struct.html#SymbolElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`graphics-object`](https://www.w3.org/TR/graphics-aam-1.0/#role-map-graphics-object) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created<br> <br>Note<br>A `symbol` element is not directly rendered, and therefore not directly exposed in the accessibility tree. However, the role (default or author-supplied) for the element<br>will be used for the rendered instance of the symbol in the use-element shadow tree. Either the `symbol` or the `use` element, or both, may have an associated<br>accessible object, depending on where the author has provided names, descriptions, roles, or interactivity. |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.58 `text`

[Permalink for Section 5.2.58](https://www.w3.org/TR/svg-aam-1.0/#role-map-text)

| SVG Specification | [`text`](https://www.w3.org/TR/SVG2/text.html#TextElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`group`](https://www.w3.org/TR/core-aam-1.1/#role-map-group) role, but with the following platform-specific API mappings:<br> [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) +<br> [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/)Role: `IA2_ROLE_PARAGRAPH`Interfaces: `IAccessibleText2`; `IAccessibleHypertext2`[UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx)Control Type: `Text`[ATK](https://developer.gnome.org/atk/stable/)Role: `ATK_ROLE_SECTION`Interfaces: `AtkText`; `AtkHypertext`[AX](https://developer.apple.com/documentation/appkit/nsaccessibility)AXRole: `AXGroup`AXSubrole: `(nil)`AXRoleDescription: `"group"`<br>Note<br>The platform mappings given above are similar to those recommended for [the HTML p element](https://www.w3.org/TR/html-aam/#el-p)<br>in the HTML Accessibility API Mappings specification \[[HTML-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-html-aam "HTML Accessibility API Mappings 1.0")\]. There is currently no WAI-ARIA role available that defines a distinct text block. However, such roles (denoting<br>paragraphs or distinct text regions) exist in many platform accessibility APIs and are therefore used instead of a generic group role. |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.59 `textPath`

[Permalink for Section 5.2.59](https://www.w3.org/TR/svg-aam-1.0/#role-map-textpath)

| SVG Specification | [`textPath`](https://www.w3.org/TR/SVG2/text.html#TextPathElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`group`](https://www.w3.org/TR/core-aam-1.1/#role-map-group) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created, but changes in<br> text styling _SHOULD_ be exposed through properties of the parent text element where supported<br> <br>Issue<br>The role mappings for `textPath` and `tspan` are [an open issue](https://www.w3.org/TR/svg-aam-1.0/#textpath-tspan-mappings-issue). |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.60 `title`

[Permalink for Section 5.2.60](https://www.w3.org/TR/svg-aam-1.0/#role-map-title)

| SVG Specification | [`title`](https://www.w3.org/TR/SVG2/struct.html#TitleElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created; see [Name and Description](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional_nd) mapping |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

#### 5.2.61 `tspan`

[Permalink for Section 5.2.61](https://www.w3.org/TR/svg-aam-1.0/#role-map-tspan)

| SVG Specification | [`tspan`](https://www.w3.org/TR/SVG2/text.html#TextElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`group`](https://www.w3.org/TR/core-aam-1.1/#role-map-group) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created, but changes in<br> text styling _SHOULD_ be exposed through properties of the parent text element where supported<br> <br>Issue<br>The role mappings for `textPath` and `tspan` are [an open issue](https://www.w3.org/TR/svg-aam-1.0/#textpath-tspan-mappings-issue). |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.62 `use`

[Permalink for Section 5.2.62](https://www.w3.org/TR/svg-aam-1.0/#role-map-use)

| SVG Specification | [`use`](https://www.w3.org/TR/SVG2/struct.html#UseElement) |
| Default Platform<br> WAI-ARIA Role Mappings | [`graphics-object`](https://www.w3.org/TR/graphics-aam-1.0/#) role mapping if the element meets the criteria for<br> [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements); otherwise, no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created<br> <br>Note<br>Note that the re-used graphics in the `use` element's shadow tree may still be included in the accessibility tree, even if the host element is not.<br>Editor's note<br>Previous drafts of this specification did not require that the re-used graphical elements be exposed directly; The `use` element was treated as an atomic object. This<br>was not consistent with the potential for interactive content or text within the re-used graphics.<br> <br>Corresponding with the change to directly expose re-used graphics, special rules for the accessible name and description of `use` elements are no longer required. |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | any role; see the [`Core Accessibility API Role Mappings`](https://www.w3.org/TR/core-aam-1.1/#mapping_role_table) and the<br> [`Graphics Accessibility API Role Mappings`](https://www.w3.org/TR/graphics-aam-1.0/#mapping_role_table) |

#### 5.2.63 `view`

[Permalink for Section 5.2.63](https://www.w3.org/TR/svg-aam-1.0/#role-map-view)

| SVG Specification | [`view`](https://www.w3.org/TR/SVG2/linking.html#ViewElement) |
| Default Platform<br> WAI-ARIA Role Mappings | no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created; see the section [SVG views](https://www.w3.org/TR/svg-aam-1.0/#mapping_view)<br> for special processing requirements |
| Allowed WAI-ARIA Roles and Platform WAI-ARIA Role Mappings | no role may be applied |

[Issue 2](https://github.com/w3c/svg-aam/issues/2): textPath and tspan need platform-specific mappings [Needs Implementer Input](https://github.com/w3c/svg-aam/issues/?q=is%3Aissue+is%3Aopen+label%3A%22Needs+Implementer+Input%22)

The use of the group role for
[`textPath`](https://www.w3.org/TR/svg-aam-1.0/#role-map-textpath)
and [`tspan`](https://www.w3.org/TR/svg-aam-1.0/#role-map-tspan)
is that of generic container for a span of text content which forms a distinct object (either because it has supplementary alternative text labels or descriptions or because it is
interactive). ARIA 1.1 does not have any roles for non-interactive spans of text.


More work is required to address whether text-specific platform accessibility API roles can more effectively serve this function. In particular, for ATK, the
`ATK_ROLE_STATIC` role is probably more appropriate than the usual mappings for `group`.


Suggestions for improved mappings would be welcome, in [GitHub Issue #2](https://github.com/w3c/svg-aam/issues/2))

## 6\. State and Property Mapping

[Permalink for Section 6.](https://www.w3.org/TR/svg-aam-1.0/#mapping_state-property)

This section describes how to expose WAI-ARIA [states](https://www.w3.org/TR/wai-aria/#dfn-state) and
[properties](https://www.w3.org/TR/wai-aria-1.3/#dfn-property). SVG user agents _MUST_ conform to the
[State and Property Mapping](https://www.w3.org/TR/core-aam-1.1/#mapping_state-property) accessibility API computational requirements in the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


In addition, the following attributes on SVG elements require special processing:

- `tabindex`
   on a rendered element (whether visible or not) is interpreted as defined in the
   [HTML Attribute State and Property Mappings](https://www.w3.org/TR/html-aam/#html-attribute-state-and-property-mappings) \[[HTML-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-html-aam "HTML Accessibility API Mappings 1.0")\].

- `viewTarget`
   on a [`view`](https://www.w3.org/TR/SVG2/linking.html#ViewElement) element creates an `aria-flowto` relationship on the associated
   `svg` element when the view is active, as defined in the [SVG views](https://www.w3.org/TR/svg-aam-1.0/#mapping_view) section.

- `xlink:title`
   on a link element affects the accessible [Name and Description](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional_nd) computation.


The `xlink` prefix is used here to refer to the XLink namespace, `http://www.w3.org/1999/xlink`. Attributes of the given names in that namespace should be processed as
described here, regardless of how the namespace is applied in markup or via script. XLink-namespaced attributes are deprecated in SVG 2 \[[SVG2](https://www.w3.org/TR/svg-aam-1.0/#bib-svg2 "Scalable Vector Graphics (SVG) 2")\], but user agents are still expected to process
them, to maintain backwards compatibility. Nonetheless, SVG 2 [requires that](https://svgwg.org/svg2-draft/linking.html#XLinkRefAttrs) the `href` attribute in the default
namespace takes precedence over the XLink equivalent if both are set on a given element. In that case, the XLink version is not valid for the purpose of the name and description computation.


The effective attribute for a given element, and therefore the state and property mapping, may be affected by declarative animation as described in the
[Animation](https://www.w3.org/TR/svg-aam-1.0/#mapping_animation) section.


## 7\. Special Processing Requiring Additional Computation

[Permalink for Section 7.](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional)

### 7.1 Name and Description

[Permalink for Section 7.1](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional_nd)

When computing an [accessible name](https://www.w3.org/TR/accname-1.1/#dfn-accessible-name) or [accessible description](https://www.w3.org/TR/accname-1.1/#dfn-accessible-description), [user agents](https://infra.spec.whatwg.org/#user-agent) _MUST_ conform to the section titled
[Text Alternative Computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_te) of the Accessible Name and Description specification \[[ACCNAME-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-accname-aam "Accessible Name and Description Computation 1.1")\], with the following modifications
for the SVG host language:


1. Replace [Hidden Not Referenced:](https://www.w3.org/TR/accname-1.2/#comp_hidden_not_referenced) with the following:


   > If the current node traversal is _not_ a result of following a `aria-labelledby` or `aria-describedby` reference, and the current node is not included in the
   >  accessibility tree according to the rules in
   >  [Excluding Elements from the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#exclude_elements)
   >  and [Including Elements in the Accessibility Tree](https://www.w3.org/TR/svg-aam-1.0/#include_elements), return the empty string.

2. Replace [step 2D](https://www.w3.org/TR/accname-1.2/#step2D) with the following:


   > Otherwise, if performing a text alternative computation for an accessible name:
   >
   >    - If the current node has at least one direct child `title` element, select the appropriate title based on the language rules for the SVG specification, and return the title
   >       text alternative as a flat string.
   >
   >    - If the current node is a link, and there was no child `title` element, but it has an `xlink:title` attribute, return the value of that attribute.
   >
   > If performing a text alternative computation for an accessible description:
   >
   >    - If the current node has at least one direct child `desc` element, select the appropriate description based on the language rules for the SVG specification, and return the
   >       concatenated text content of the description.

3. In [step 2F](https://www.w3.org/TR/accname-1.2/#step2F), modify [step iii](https://www.w3.org/TR/accname-1.2/#step2F.ii)
    by replacing:


   > For each child node of the current node:


    with


   > If the element is a text container element, for each child node of the current node:

4. Replace [step 2H](https://www.w3.org/TR/accname-1.2/#step2H) with the following:


   > Otherwise, if performing a text alternative computation for an accessible description, and the current node has at least one direct child `title` element, but the title
   > elements were _not_ used when generating the accessible name for the node, then select the appropriate title based on the language rules for the SVG specification, and return
   > the title text content as the description.
   >
   >
   > Otherwise, if the current node is a link, and it has an `xlink:title` attribute that was not used for the accessible name, return the value of that attribute.


When determining whether an element has a _direct child_ element, only actual DOM child elements are considered, regardless of whether or not the parent element has an associated
shadow tree.


Note

The net effect of these changes is to establish the following priority of alternative text values for the accessible name:

1. `aria-labelledby`
2. `aria-label`
3. a direct child `title` element
4. `xlink:title` attribute on a link
5. for text container elements, the text content

The alternative text values for the accessible description have the following priority:

1. `aria-describedby`
2. a direct child `desc` element
3. for text container elements, the text content
4. a direct child `title` element that provides a tooltip, when ARIA label attributes are used to provide the accessible name
5. `xlink:title` attribute on a link, if not used to provide the accessible name

The `aria-labelledby` and `aria-describedby` properties can reference the element on which they are given, in order to concatenate one of the other text alternatives
with text from a separate element.


### 7.2 Widget Values

[Permalink for Section 7.2](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional_widget-value)

SVG user agents _MUST_ conform to the
[Widget Values](https://www.w3.org/TR/core-aam-1.1/#mapping_additional_widget-value)
accessibility API computational requirements in the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


### 7.3 Relations

[Permalink for Section 7.3](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional_relations)

SVG user agents _MUST_ conform to the
[Relations](https://www.w3.org/TR/core-aam-1.1/#mapping_additional_relations)
accessibility API computational requirements in the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


Issue

The CORE-AAM section on Relations requires that assistive technologies _SHOULD_ provide a method to navigate to (and within) structured content referenced by `aria-describedby`.
This conflicts with the current approach of not including non-rendered descriptive content in the accessibility tree.


[See the issue discussion for that specification](https://github.com/w3c/core-aam/issues/3), and the
[related issue about exposing SVG`desc` content](https://github.com/w3c/svg-aam/issues/6).


### 7.4 Group Position

[Permalink for Section 7.4](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional_position)

SVG user agents _MUST_ conform to the
[Group Position](https://www.w3.org/TR/core-aam-1.1/#mapping_additional_position)
accessibility API computational requirements in the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


### 7.5 Use-Element Shadow Trees

[Permalink for Section 7.5](https://www.w3.org/TR/svg-aam-1.0/#mapping_use_shadow_tree)

This specification uses the terms
[shadow tree](https://dom.spec.whatwg.org/#concept-shadow-tree)
and [host](https://dom.spec.whatwg.org/#concept-documentfragment-host)
as defined by the DOM standard \[[DOM](https://www.w3.org/TR/svg-aam-1.0/#bib-dom "DOM Standard")\], and the terms
[use-element shadow tree](https://www.w3.org/TR/SVG2/struct.html#TermUseElementShadowTree)
and [element instance](https://www.w3.org/TR/SVG2/struct.html#TermElementInstance)
as defined by SVG 2 \[[SVG2](https://www.w3.org/TR/svg-aam-1.0/#bib-svg2 "Scalable Vector Graphics (SVG) 2")\].


SVG user agents _MUST_ process the element instances generated for the use-element shadow tree as if those elements were children of the `use` element itself, with the following
conditions:


- When processing WAI-ARIA attributes on elements within a shadow tree, the user agent _MUST_ first attempt to match any IDREF values against other elements in the same shadow tree, before
   searching for a match in the host's node tree. If shadow trees are nested, the user agent _MUST_ recursively search from the current shadow tree to the tree containing its host
   `use` element, until the document tree is reached.


- In all other cases, when matching IDREF values in WAI-ARIA attributes, the user agent _MUST NOT_ consider elements in the shadow tree of a `use` element.


[Issue 7](https://github.com/w3c/svg-aam/issues/7): Harmonize use-element behavior with other shadow DOM behavior [Needs ARIA WG Input](https://github.com/w3c/svg-aam/issues/?q=is%3Aissue+is%3Aopen+label%3A%22Needs+ARIA+WG+Input%22) [Needs Implementer Input](https://github.com/w3c/svg-aam/issues/?q=is%3Aissue+is%3Aopen+label%3A%22Needs+Implementer+Input%22)

The editors will be working to harmonize these guidelines with general rules for WAI-ARIA processing of shadow tree elements, such as in web components. Feedback from implementers is
requested on the practical feasibility of encapsulating IDREF matching in this manner.


General feedback on shadow DOM and ARIA should be discussed
[in the Core-AAM issue](https://github.com/w3c/core-aam/issues/4). Feedback unique to SVG can be submitted [to Issue #7](https://github.com/w3c/svg-aam/issues/7) on
this specification.


### 7.6 SVG Views

[Permalink for Section 7.6](https://www.w3.org/TR/svg-aam-1.0/#mapping_view)

SVG provides authors with the means of specifying a particular
[view of the document](https://svgwg.org/svg2-draft/linking.html#LinksIntoSVG). A view is applied through the target fragment of the document URL, either by referencing the id of
a [`view`](https://www.w3.org/TR/SVG2/linking.html#ViewElement) element, or by specifying a custom view using the SVG view specification
fragment identifier.


The visual effect of an SVG view is equivalent to modifying attributes on the parent `svg` element (for a `view` element) or the root element (for an SVG view
specification fragment). User agents _SHOULD_ therefore modify the [accessible object](https://www.w3.org/TR/wai-aria-1.3/#dfn-accessible-object) representing that
`svg`
when a view is in effect.


In particular, the following changes should be made:

- If the view includes a `viewTarget` attribute, the `svg` element _SHOULD_ be mapped as if it had an `aria-flowto` attribute specifying the same list of IDREF
   values contained in the `viewTarget` attribute.

- If the view is applied using a `view` element, compute the accessible name and description for that element, ignoring the fact that a `view` element is excluded from
   the accessibility tree. If the result is a non-empty string, it _SHOULD_ replace the corresponding name or description for the `svg` element while the view is in effect.


A navigation action towards a URL including an SVG view specification or the id of a `view` element _SHOULD_ be treated as a series of property change
events on the target `svg` element followed by navigation to that element. User agents _MAY_ represent the property changes as the deletion of existing
nodes followed by the insertion of modified nodes.


[Issue 8](https://github.com/w3c/svg-aam/issues/8): Exposing SVG view behavior and viewTarget to accessibility APIs [Needs Implementer Input](https://github.com/w3c/svg-aam/issues/?q=is%3Aissue+is%3Aopen+label%3A%22Needs+Implementer+Input%22)

SVG Views provide a functionality unique to SVG, with no direct equivalent in HTML documents. They may be used as the end-point of a navigation action, but are not themselves a container
for the targeted content. They may also be used at the time an SVG document is embedded, to subset the visual content to only include a portion of the file.


The editors would be very interested in practical examples of SVG views in use, so that we may determine if the above requirements are sufficient. Particular issues to consider include
whether special rules are required for managing keyboard focus, or for excluding content that is rendered offscreen when a view is in effect.


In addition, the `viewTarget` attribute, and the corresponding parameter for SVG view fragments, has been deprecated in SVG 2\. Their intended use, to trigger visual styling
changes in the target element, has never been well implemented by user agents. Without `viewTarget`, there would be no native way in SVG to indicate the semantic target of a
given view. For `view` elements (but not view fragments), a possible alternative is to encourage authors to directly specify `aria-flowsto` attributes. These would
then need to be mapped to the relevant `svg` element.


This raises the question of whether any other (or all) ARIA attributes should be mapped from the `view` element onto the accessible object for the `svg` element while
the view is in effect. This would require careful consideration of all possible consequences and conflicts. For example, should a view be able to change the role of the SVG element?


The `aria-flowsto` attribute is not well supported in assistive tools; there have been proposals to deprecate it in a future version. Are there other ways in which user agents
could expose the changed view, so that users of assistive technologies can quickly understand which parts of the graphic are visible?


Feedback on any of these points can be provided
[on issue #8](https://github.com/w3c/svg-aam/issues/8).


### 7.7 Declarative Animation

[Permalink for Section 7.7](https://www.w3.org/TR/svg-aam-1.0/#mapping_animation)

SVG animation elements may modify element attributes and style properties. CSS animations may modify style properties. Either type of animation may be triggered by user interaction, or may
run on a fixed schedule.


If an animation changes the effective value of a WAI-ARIA state or property attribute, or an SVG attribute that is described in the
[State and Property Mapping](https://www.w3.org/TR/svg-aam-1.0/#mapping_state-property) section, the User Agent _MUST_ expose the change in the same way as if the actual attribute value was changed.


Note

The `role` attribute is not animatable.

If an animated change affects whether an element is rendered, or change whether it is visible in a way that would cause it to be excluded from the accessibility tree, user agents
_SHOULD_ expose the change according to the guidelines in the
[Changes to document content or node visibility](https://www.w3.org/TR/core-aam-1.1/#mapping_events_visibility) section of the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


## 8\. Actions

[Permalink for Section 8.](https://www.w3.org/TR/svg-aam-1.0/#mapping_actions)

SVG user agents _MUST_ conform to the
[Actions](https://www.w3.org/TR/core-aam-1.1/#mapping_actions)
accessibility API computational requirements in the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


## 9\. Events

[Permalink for Section 9.](https://www.w3.org/TR/svg-aam-1.0/#mapping_events)

[user agents](https://infra.spec.whatwg.org/#user-agent) fire [events](https://www.w3.org/TR/wai-aria-1.3/#dfn-event) for user actions,
WAI-ARIA [state](https://www.w3.org/TR/wai-aria-1.3/#dfn-state) changes, changes to document content or node visibility, changes in selection, and operation of menus. Conforming user agents
_MUST_ support the \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\] [Events](https://www.w3.org/TR/core-aam-1.1/#mapping_events) mappings.


## 10\. Special Document Handling Procedures

[Permalink for Section 10.](https://www.w3.org/TR/svg-aam-1.0/#document-handling)

SVG user agents _MUST_ conform to the
[Special Document Handling Procedures](https://www.w3.org/TR/core-aam-1.1/#document-handling)
in the Core Accessibility API Mappings \[[CORE-AAM](https://www.w3.org/TR/svg-aam-1.0/#bib-core-aam "Core Accessibility API Mappings 1.1")\].


## 11\. Security and Privacy Considerations

[Permalink for Section 11.](https://www.w3.org/TR/svg-aam-1.0/#security-privacy)

Implementation of this specification is not expected to add any new security or privacy considerations to the web platform, relative to implementation of SVG (\[[SVG2](https://www.w3.org/TR/svg-aam-1.0/#bib-svg2 "Scalable Vector Graphics (SVG) 2")\]) and WAI-ARIA
(\[[WAI-ARIA](https://www.w3.org/TR/svg-aam-1.0/#bib-wai-aria "Accessible Rich Internet Applications (WAI-ARIA) 1.1")\]) separately.


Editor's note

If you believe there is a potential new security or privacy risk created by this specification, please [raise an issue](https://github.com/w3c/svg-aam/issues)
in the specification's GitHub repository.


## A. Appendices

[Permalink for Appendix A.](https://www.w3.org/TR/svg-aam-1.0/#appendices)

### A.1 Acknowledgments

[Permalink for Appendix A.1](https://www.w3.org/TR/svg-aam-1.0/#acknowledgements)

_This section is non-normative._

In addition to the credited authors and editors, the participants in the SVG Accessibility Task Force contributed to the development of this document. Appreciation also goes to Joanmarie
Diggs and other implementers who have offered feedback on the drafts and helped with testing.


#### A.1.1 ARIA WG Participants at the time of publication

[Permalink for Appendix A.1.1](https://www.w3.org/TR/svg-aam-1.0/#ack_group)

- Rahim Abdi (Apple Inc.)
- NAVYA AGARWAL (Adobe)
- Joey Arhar (Google LLC)
- Bernardo Barlach (Google LLC)
- Benjamin Beaudry (Microsoft Corporation)
- Zoë Bijl (W3C Invited Experts)
- Gautier Chomel (EDRLab)
- Aleksandar Cindrikj (Netcetera)
- Keith Cirkel (Mozilla.org)
- Daniel Clark (Microsoft Corporation)
- James Craig (Apple Inc.)
- Diego Della Rossa (UsableNet)
- Joanmarie Diggs (Igalia)
- Tamsin Ewing (W3C)
- Mayuri Faldu (Navy Federal Credit Union)
- Betsy Fanning (PDF Association)
- Steve Faulkner (TetraLogical Services Ltd)
- Patrick Foster (axes4 GmbH)
- Jane Fulton (Cisco)
- Bryan Garaventa (W3C Invited Experts)
- Matt Garrish (DAISY Consortium)
- Doug Geoffray (Microsoft Corporation)
- Ariella Gilmore (IBM Corporation)
- Taylore Givens (Microsoft Corporation)
- David Grogan (Google LLC)
- Shirisha Gubba (W3C Invited Experts)
- Jon Gunderson (University of Illinois)
- Oliver Habersetzer (SAP SE)
- Theo Hale (W3C Invited Experts)
- Sunny Hardasani (Adobe)
- Matthew Hardy (Adobe)
- Chris Harrelson (Google LLC)
- Sarah Higley (Microsoft Corporation)
- Hans Hillen (TPGi)
- takumi hiramatsu (Cybozu)
- Stanley Hon (Microsoft Corporation)
- Michael Jackson (Microsoft Corporation)
- John Jansen (Microsoft Corporation)
- Jilin Jiang (Ant Group Co., Ltd.)
- Duff Johnson (PDF Association)
- Summer Jones (Thomson Reuters Corp.)
- Yuki Kamahori (Cybozu)
- William Kilian (Kilian Codes LLC)
- Matthew King (W3C Invited Experts)
- Zachary Kinsey (TargetStream Technologies)
- Daisuke Kobayashi (Cybozu)
- Peter Krautzberger (krautzource UG)
- Nina Krauß (SAP SE)
- JaEun Jemma Ku (University of Illinois)
- Ugi Kutluoglu (Oracle Corporation)
- Steven Lambert (Deque Systems, Inc.)
- Joe Lamyman (TetraLogical Services Ltd)
- Charles LaPierre (Benetech)
- Patrick Lauke (TetraLogical Services Ltd)
- Philip Lazarevic (Level Access)
- Leo Lee (Microsoft Corporation)
- Brett Lewis (TPGi)
- Alison Maher (Microsoft Corporation)
- Gurpreet Kaur Mangera (Rakuten Group, Inc.)
- Mark McCarthy (University of Illinois)
- Katie McDermott (See Me Please)
- Eduardo Meza Etienne (Navy Federal Credit Union)
- Clay Miller (Microsoft Corporation)
- Hirotaka Minamida (Cybozu)
- Daniel Montalvo (W3C)
- Baldino Morelli (UsableNet)
- Jacques Newman (Microsoft Corporation)
- James Nurthen (Evinced Inc.)
- Scott O'Hara (Microsoft Corporation)
- Lola Odelola (W3C Invited Experts)
- Neil Osman (Evinced Inc.)
- Yusuke Oyama (Cybozu)
- Adam Page (Hilton)
- Michael Pennisi (Igalia)
- Giacomo Petri (UsableNet)
- Noah Praskins (TPGi)
- Lucas Radaelli (Google LLC)
- Paul Rayius (PDFix-US)
- Mark Rogers (Powermapper Software)
- Adrian Roselli (W3C Invited Experts)
- Marco Sabidussi (UsableNet)
- Trisha Salas (Level Access)
- Stefan Schnabel (SAP SE)
- Harris Schneiderman (Deque Systems, Inc.)
- Raymond Schwartz (Navy Federal Credit Union)
- Kyra Seevers (Google LLC)
- Davis Shaver (The Washington Post)
- Cynthia Shelly (W3C Invited Experts)
- Tzviya Siegman (W3C)
- Avneesh Singh (DAISY Consortium)
- Michael\[tm\] Smith (sideshowbarker) (W3C)
- Francis Storr (Intel Corporation)
- Nobukiyo Sugisaki (Cybozu)
- Melanie Sumner (IBM Corporation)
- Alexander Surkov (Igalia)
- James Teh (Mozilla.org)
- Roman Toda (Foxit software)
- David Tseng (Google LLC)
- Cybozu W3C (Cybozu)
- Tyler Wilcock (Apple Inc.)

#### A.1.2 Past participants in the SVG Accessibility Task Force

[Permalink for Appendix A.1.2](https://www.w3.org/TR/svg-aam-1.0/#ack_taskforce)

- Amelia Bellamy-Royds
- Michael Cooper (W3C)
- Erik Dahlström (Opera)
- Amy Dai (Oracle Corporation)
- Fred Esch (IBM Corporation)
- Charles McCathie Nevile (Yandex)
- Cameron McCormack (Mozilla Foundation)
- Brian McNeily (SSB BART Group)
- Heather Migliorisi
- Charu Pandhi (IBM Corporation)
- Janina Sajka
- Doug Schepers (W3C)
- Rich Schwerdtfeger (Knowbility)
- Léonie Watson (The Paciello Group, LLC)
- Jason White (Educational Testing Service)

#### A.1.3 Enabling funders

[Permalink for Appendix A.1.3](https://www.w3.org/TR/svg-aam-1.0/#ack_funders)

This publication has been funded in part with U.S. Federal funds from the Department of Education, National Institute on Disability, Independent Living, and Rehabilitation Research (NIDILRR), initially under contract number ED-OSE-10-C-0067, then under contract number HHSP23301500054C, and now under HHS75P00120P00168. The content of this publication does not necessarily reflect the views or policies of the U.S. Department of Education, nor does mention of trade names, commercial products, or organizations imply endorsement by the U.S. Government.

### A.2 Issue summary

[Permalink for Appendix A.2](https://www.w3.org/TR/svg-aam-1.0/#issue-summary)

- [Issue 6](https://www.w3.org/TR/svg-aam-1.0/#issue-container-number-6): Should structured descriptions be exposed in the accessibility tree?
- [Issue](https://www.w3.org/TR/svg-aam-1.0/#issue-container-generatedID-10)
- [Issue](https://www.w3.org/TR/svg-aam-1.0/#issue-container-generatedID-11)
- [Issue 2](https://www.w3.org/TR/svg-aam-1.0/#textpath-tspan-mappings-issue): textPath and tspan need platform-specific mappings
- [Issue](https://www.w3.org/TR/svg-aam-1.0/#issue-container-generatedID-15)
- [Issue 7](https://www.w3.org/TR/svg-aam-1.0/#issue-container-number-7): Harmonize use-element behavior with other shadow DOM behavior
- [Issue 8](https://www.w3.org/TR/svg-aam-1.0/#issue-container-number-8): Exposing SVG view behavior and viewTarget to accessibility APIs

## B. References

[Permalink for Appendix B.](https://www.w3.org/TR/svg-aam-1.0/#references)

### B.1 Normative references

[Permalink for Appendix B.1](https://www.w3.org/TR/svg-aam-1.0/#normative-references)

\[ACCNAME-AAM\][Accessible Name and Description Computation 1.1](https://www.w3.org/TR/accname-1.1/). Joanmarie Diggs; Bryan Garaventa; Michael Cooper. W3C. 18 December 2018. W3C Recommendation. URL: [https://www.w3.org/TR/accname-1.1/](https://www.w3.org/TR/accname-1.1/)\[CORE-AAM\][Core Accessibility API Mappings 1.1](https://www.w3.org/TR/core-aam-1.1/). Joanmarie Diggs; Joseph Scheuhammer; Richard Schwerdtfeger; Michael Cooper; Andi Snow-Weaver; Aaron Leventhal. W3C. 14 December 2017. W3C Recommendation. URL: [https://www.w3.org/TR/core-aam-1.1/](https://www.w3.org/TR/core-aam-1.1/)\[CSS-CASCADE-3\][CSS Cascading and Inheritance Level 3](https://www.w3.org/TR/css-cascade-3/). Elika Etemad; Tab Atkins Jr. W3C. 11 February 2021. W3C Recommendation. URL: [https://www.w3.org/TR/css-cascade-3/](https://www.w3.org/TR/css-cascade-3/)\[DOM\][DOM Standard](https://dom.spec.whatwg.org/). Anne van Kesteren. WHATWG. Living Standard. URL: [https://dom.spec.whatwg.org/](https://dom.spec.whatwg.org/)\[GRAPHICS-AAM\][Graphics Accessibility API Mappings](https://www.w3.org/TR/graphics-aam-1.0/). Amelia Bellamy-Royds; Joanmarie Diggs; Michael Cooper. W3C. 2 October 2018. W3C Recommendation. URL: [https://www.w3.org/TR/graphics-aam-1.0/](https://www.w3.org/TR/graphics-aam-1.0/)\[HTML-AAM\][HTML Accessibility API Mappings 1.0](https://www.w3.org/TR/html-aam-1.0/). Scott O'Hara; Rahim Abdi. W3C. 12 October 2026. W3C Working Draft. URL: [https://www.w3.org/TR/html-aam-1.0/](https://www.w3.org/TR/html-aam-1.0/)\[infra\][Infra Standard](https://infra.spec.whatwg.org/). Anne van Kesteren; Domenic Denicola. WHATWG. Living Standard. URL: [https://infra.spec.whatwg.org/](https://infra.spec.whatwg.org/)\[rfc2119\][Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/info/rfc2119/). S. Bradner. IETF. March 1997. Best Current Practice. URL: [https://www.rfc-editor.org/info/rfc2119/](https://www.rfc-editor.org/info/rfc2119/)\[RFC8174\][Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/info/rfc8174/). B. Leiba. IETF. May 2017. Best Current Practice. URL: [https://www.rfc-editor.org/info/rfc8174/](https://www.rfc-editor.org/info/rfc8174/)\[SVG1\][Scalable Vector Graphics (SVG) 1.0 Specification](https://www.w3.org/TR/SVG/). Jon Ferraiolo. W3C. 4 September 2001. W3C Recommendation. URL: [https://www.w3.org/TR/SVG/](https://www.w3.org/TR/SVG/)\[SVG11\][Scalable Vector Graphics (SVG) 1.1 (Second Edition)](https://www.w3.org/TR/SVG11/). Erik Dahlström; Patrick Dengler; Anthony Grasso; Chris Lilley; Cameron McCormack; Doug Schepers; Jonathan Watt; Jon Ferraiolo; Jun Fujisawa; Dean Jackson et al. W3C. 16 August 2011. W3C Recommendation. URL: [https://www.w3.org/TR/SVG11/](https://www.w3.org/TR/SVG11/)\[SVG2\][Scalable Vector Graphics (SVG) 2](https://www.w3.org/TR/SVG2/). Karl Dubost; Dirk Schulze; Divyansh Mangal; Virali Purbey. W3C. 6 October 2026. W3C Candidate Recommendation. URL: [https://www.w3.org/TR/SVG2/](https://www.w3.org/TR/SVG2/)\[WAI-ARIA\][Accessible Rich Internet Applications (WAI-ARIA) 1.1](https://www.w3.org/TR/wai-aria-1.1/). Joanmarie Diggs; Shane McCarron; Michael Cooper; Richard Schwerdtfeger; James Craig. W3C. 14 December 2017. W3C Recommendation. URL: [https://www.w3.org/TR/wai-aria-1.1/](https://www.w3.org/TR/wai-aria-1.1/)

### B.2 Informative references

[Permalink for Appendix B.2](https://www.w3.org/TR/svg-aam-1.0/#informative-references)

\[accname\][Accessible Name and Description Computation 1.1](https://www.w3.org/TR/accname-1.1/). Joanmarie Diggs; Bryan Garaventa; Michael Cooper. W3C. 18 December 2018. W3C Recommendation. URL: [https://www.w3.org/TR/accname-1.1/](https://www.w3.org/TR/accname-1.1/)\[AT-SPI\][Assistive Technology Service Provider Interface](https://gnome.pages.gitlab.gnome.org/at-spi2-core/libatspi/). The GNOME Project. URL: [https://gnome.pages.gitlab.gnome.org/at-spi2-core/libatspi/](https://gnome.pages.gitlab.gnome.org/at-spi2-core/libatspi/)\[ATK\][ATK - Accessibility Toolkit](https://developer.gnome.org/atk/stable/). The GNOME Project. URL: [https://developer.gnome.org/atk/stable/](https://developer.gnome.org/atk/stable/)\[AXAPI\][The NSAccessibility Protocol for macOS](https://developer.apple.com/documentation/appkit/nsaccessibility). Apple, Inc. URL: [https://developer.apple.com/documentation/appkit/nsaccessibility](https://developer.apple.com/documentation/appkit/nsaccessibility)\[GRAPHICS-ARIA\][WAI-ARIA Graphics Module](https://www.w3.org/TR/graphics-aria-1.0/). Amelia Bellamy-Royds; Joanmarie Diggs; Michael Cooper. W3C. 2 October 2018. W3C Recommendation. URL: [https://www.w3.org/TR/graphics-aria-1.0/](https://www.w3.org/TR/graphics-aria-1.0/)\[IAccessible2\][IAccessible2](https://wiki.linuxfoundation.org/accessibility/iaccessible2/). Linux Foundation. URL: [https://wiki.linuxfoundation.org/accessibility/iaccessible2/](https://wiki.linuxfoundation.org/accessibility/iaccessible2/)\[MSAA\][Microsoft Active Accessibility (MSAA)](https://docs.microsoft.com/en-us/windows/win32/winauto/microsoft-active-accessibility). Microsoft Corporation. URL: [https://docs.microsoft.com/en-us/windows/win32/winauto/microsoft-active-accessibility](https://docs.microsoft.com/en-us/windows/win32/winauto/microsoft-active-accessibility)\[UI-AUTOMATION\][UI Automation](https://docs.microsoft.com/en-us/windows/win32/winauto/ui-automation-specification). Microsoft Corporation. URL: [https://docs.microsoft.com/en-us/windows/win32/winauto/ui-automation-specification](https://docs.microsoft.com/en-us/windows/win32/winauto/ui-automation-specification)\[WAI-ARIA-10\][Accessible Rich Internet Applications (WAI-ARIA) 1.0](https://www.w3.org/TR/wai-aria/). James Craig; Michael Cooper et al. W3C. 20 March 2014. W3C Recommendation. URL: [https://www.w3.org/TR/wai-aria/](https://www.w3.org/TR/wai-aria/)

[↑](https://www.w3.org/TR/svg-aam-1.0/#title)