
# sphinx-design stuff

## Icons

{octicon}`heart-fill;1em;sd-text-danger`

## Tabs

````{tab-set}
```{tab-item} Label1
Markdown 1
```

```{tab-item} Label2
Markdown 2
```
````

## Dropdowns

```{dropdown}
Dropdown content
```

```{dropdown} Dropdown title
Dropdown content
```

```{dropdown} Open dropdown
:open:

Dropdown content
```

## Shadows

```{dropdown} Default Shadow
Dropdown content
```

```{dropdown} "sm" Shadow
:class-container: sd-shadow-sm

Dropdown content
```

```{dropdown} "md" Shadow
:class-container: sd-shadow-md

Dropdown content
```

```{dropdown} "lg" Shadow
:class-container: sd-shadow-lg

Dropdown content
```

## Cards

```{card} Card Title
Header
^^^
Card content
+++
Footer
```

```{card} Clickable Card (external)
:link: https://example.com

The entire card can be clicked to navigate to <https://example.com>.
```

## Carousels

````{card-carousel} 2

```{card} card 1
```

```{card} card 2
```

```{card} card 3
```

```{card} card 4
```

```{card} card 5
```

```{card} card 6
```

````

## Article Info

```{article-info}
:avatar: https://pbs.twimg.com/profile_images/1316325058499944448/mIOSbACJ_400x400.jpg
:avatar-link: https://errbufferoverfl.me
:avatar-outline: muted
:author: errbufferoverfl
:date: Aug 15, 2021
:read-time: 5 min read
```

## Badges

{bdg}`plain badge`

{bdg-primary}`primary` {bdg-primary-line}`primary-line`

{bdg-secondary}`secondary` {bdg-secondary-line}`secondary-line`

{bdg-success}`success` {bdg-success-line}`success-line`

{bdg-info}`info` {bdg-info-line}`info-line`

{bdg-warning}`warning` {bdg-warning-line}`warning-line`

{bdg-danger}`danger` {bdg-danger-line}`danger-line`

{bdg-light}`light` {bdg-light-line}`light-line`

{bdg-dark}`dark` {bdg-dark-line}`dark-line`

## Buttons

```{button-link} https://example.com
Button text
```

```{button-link} https://example.com
:color: primary
Button text
```

```{button-link} https://example.com
:color: secondary
:expand:
```